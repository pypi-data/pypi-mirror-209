import nltk

import os
import sys
import re
import fnmatch
from time import strftime
import csv
import gc
import psutil
import subprocess
import pkg_resources

from collections import OrderedDict

import multiprocessing as mp
from multiprocessing import Pool
from functools import partial

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

import pandas as pd
import itertools
import numpy as np

from bs4 import BeautifulSoup as BS

import zipfile as zf
import unicodedata
from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone

import enchant
from enchant.checker import SpellChecker
from enchant.tokenize import EmailFilter, URLFilter

import random
random.seed(1000)

import pickle
import mapply
import multiprocess.context as ctx
ctx._force_start_method('spawn')
import collections
from typing import Tuple, List
import pkg_resources


import warnings
warnings.filterwarnings('ignore', message = '.*looks like a URL.*', category = UserWarning, module = 'bs4')

# initialize mapply
useCores = mp.cpu_count()
mapply.init(
    n_workers = useCores) # chunk_size = 5

### Setup NLP Tools ###

# SentiWN #
from nltk.corpus import sentiwordnet as swn
swn.ensure_loaded()

import pkg_resources

wnaffect_path = pkg_resources.resource_filename('textagon', 'external/extracted/WNAffect-master')
wordnet_path = pkg_resources.resource_filename('textagon', 'external/extracted/wordnet-1.6')
wn_domains_path = pkg_resources.resource_filename('textagon', 'external/extracted/wn-domains')

sys.path.append(wnaffect_path)
from wnaffect import WNAffect
from emotion import Emotion
wna = WNAffect(wordnet_path, wn_domains_path)

# VADER #
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# spaCy #
import spacy
nlp = spacy.load('en_core_web_sm', exclude = ['lemmatizer'])
nlp.max_length = 10 ** 10

def spaCyTOK (sentence):

    doc = nlp.tokenizer(sentence)
    tokens = []
    for token in doc:
        tokens.append(token.text)
    return(tokens)

def splitWS (sentence):
    return(sentence.split(' '))

def vector_hasher(x):
    return hash(tuple(x))

pkg_resources.require('wn==0.0.23') # for pywsd

class SuppressStdErr:
    def __enter__ (self):
        self._original_stderr = sys.stderr
        sys.stderr = open(os.devnull, 'w')

    def __exit__ (self, exc_type, exc_val, exc_tb):
        sys.stderr.close()
        sys.stderr = self._original_stderr

with SuppressStdErr():
    import pywsd
    from pywsd import disambiguate
    from pywsd.lesk import adapted_lesk

### Below are functions to run ###

def say_hello():
    print("Hello, World!")

def setSpellChecking(exclusionsFileFullPath='None'):
    b = enchant.Broker()
    spellcheckerLibrary = 'en'
    b.set_ordering(spellcheckerLibrary, 'aspell')

    if exclusionsFileFullPath == 'None':
        # Use the default exclusions file
        exclusionsFileFullPath = pkg_resources.resource_filename('textagon', 'external/lexicons/exclusions.txt')
    elif not os.path.isfile(exclusionsFileFullPath):
        print('Provided exclusions file does not exist. Switching to default exclusions file.')
        # Switch to the default exclusions file if the provided one does not exist
        exclusionsFileFullPath = pkg_resources.resource_filename('textagon', 'external/lexicons/exclusions.txt')

    try:
        spellchecker = enchant.DictWithPWL(spellcheckerLibrary, pwl = exclusionsFileFullPath, broker = b)

        exclusionsFile = open(exclusionsFileFullPath, 'r')
        exclusionsLength = len(exclusionsFile.readlines())
        exclusionsFile.close()

        print('# Spellchecker Details #')
        print('Provider:', spellchecker.provider)
        print('Enchant Version:', enchant.get_enchant_version())
        print('Dictionary Tag:', spellchecker.tag)
        print('Dictionary Location:', spellchecker.provider.file)
        print('Total Exclusions: ' + str(exclusionsLength))

        # Return the values
        return spellcheckerLibrary, exclusionsFileFullPath, exclusionsLength, spellchecker
    except Exception as e:
        print(f'Error opening or reading file {exclusionsFileFullPath}: {e}')
        return None, None, 0, None

def ReadAllLexicons(lexiconFileFullPath=None):

    # Get the path of the default lexicon file
    if lexiconFileFullPath is None:
        print('No lexicon file provided. Using default lexicon file.')
        lexiconFileFullPath = pkg_resources.resource_filename('textagon', 'external/lexicons/Lexicons_v5.zip')

    def is_valid_zip_file(file_path):
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            print("Please ensure that you provide the full path to the file.")
            print('Example path looks like: C:/paht/to/zip/file/lexicon.zip')
            return False
        # Check if file is a zip file
        if not zf.is_zipfile(file_path):
            print(f"Error: The file '{file_path}' is not a valid zip file.")
            return False
        return True

    if not is_valid_zip_file(lexiconFileFullPath):
        return False
    
    customLexicons = {}

    def BuildLexicon (L, customLexicons):

        tagTokenPairs = list(filter(None, L.split('\n')))

        #print(tagTokenPairs)

        for i, tagTokenPair in enumerate(tagTokenPairs):
            elements = tagTokenPair.split('\t')
            tag = elements[0].strip().upper()
            #print(tag)
            #print(elements)
            tokens = elements[1].lower().split(',')
            tokens = [x.strip() for x in tokens]

            # add every lexicon word to spell checker (not used)
            '''
            for each in tokens:
                spellchecker.add(each)
            '''

            if i == 0:
                customLexicons[os.path.splitext(os.path.basename(file))[0].upper() ] = {tag: tokens}
            else:
                customLexicons[os.path.splitext(os.path.basename(file))[0].upper() ][tag] = tokens

        return(customLexicons)

    zipFile = zf.ZipFile(lexiconFileFullPath, 'r')
    for file in sorted(zipFile.namelist()):
        if fnmatch.fnmatch(file, '*.txt'):
            L = zipFile.read(file).decode('utf-8').encode('utf-8').decode('unicode-escape')
            customLexicons = BuildLexicon(L, customLexicons)
    print('# Custom Lexicons Imported:', len(customLexicons), '#')

    # sort lexicon names alphabetically
    customLexicons = OrderedDict(sorted(customLexicons.items()))

    if len(customLexicons) != 0:
        for key, value in customLexicons.items():

            # sort lexicon tags alphabetically
            customLexicons[key] = OrderedDict(sorted(value.items()))

            print('-', key, '(' + str(len(value)) + ' Tags)')
    print('\r')

    return(customLexicons)

def SanityCheck(dataPath: str = None, override_original_file: bool = False) -> Tuple[int, dict, List[Tuple[str, str]]]:
    print("Sanity check started...")
    def is_valid_file(file_path: str) -> bool:
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist. Please ensure that you provide the full path to the file.")
            return False
        return True
    
    if not is_valid_file(dataPath):
        return -1, {}, []

    spellchecker = enchant.Dict("en_US")
    classes_counter = collections.Counter()
    raw_data = []

    with open(dataPath, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) != 2:
            print(f"Error: Invalid format on line '{line.strip()}', each line should contain exactly two parts separated by a tab.")
            print('Please make sure your data have labels in first column and text in second column.')
            break

        label, text = parts
        classes_counter[label] += 1

        words = re.findall(r'\b\w+\b', text)
        checked_text = " ".join(word for word in words if spellchecker.check(word))

        raw_data.append((label, checked_text))

    num_classes = len(classes_counter)
    samples_per_class = dict(classes_counter)

    if override_original_file:
        with open(dataPath, 'w') as f:
            for label, text in raw_data:
                f.write(f"{label}\t{text}\n")
    print(f"Sanity check completed, found {num_classes} classes and {len(raw_data)} samples.")

    ret_dict = {
        'num_classes': num_classes,
        'samples_per_class': samples_per_class,
        'raw_data': raw_data
    }

    return ret_dict

def ReadRawText (path: str = None):
    print("Reading raw text...")
    pure_chunck = SanityCheck(dataPath=path, override_original_file=False)
    classLabels = list(pure_chunck['samples_per_class'].keys())
    raw = [x[1] for x in pure_chunck['raw_data']]
    print("Reading raw text completed.")
    return({'corpus': raw, 'classLabels': classLabels})

def TextToFeatures (textData, debug = False, lexicons = None, wnaReturnLevel = 5, useSpellChecker = True, provideMisspellingDetailed = True, useCores = 1):

    if lexicons == None:
        lexicons = ReadAllLexicons()
    else:
        if isinstance(lexicons, str):
            if os.path.exists(lexicons):
                lexicons = ReadAllLexicons(lexiconFileFullPath=lexicons)
        elif isinstance(lexicons, collections.OrderedDict):
            pass
        else:
            print('Lexicons must be a path to lexicon zip file or an well-done lexicon OrderedDict.')
            return None

    spellcheckerLibrary, exclusionsFileFullPath, exclusionsLength, spellchecker = setSpellChecking(exclusionsFileFullPath=exclusionsFileFullPath)

    textData = pd.DataFrame({
        'InitialSentence': textData
        })

    def BasicTextCleanup (sentence, debug = False):

        if debug:
            print('\nInitial Sentence:', sentence)

        # note: need to add exception handler (e.g., non-English issues)

        # Basic Cleaning
        initialSentenceLength = len(sentence)

        # Strip html
        sentence = BS(sentence, 'html.parser').get_text()
        htmlStripLength = initialSentenceLength - len(sentence)

        # Strip all excessive whitespace (after html to ensure no additional spaces result from html stripping)
        sentence = ' '.join(sentence.split())
        whitespaceStripLength = initialSentenceLength - htmlStripLength - len(sentence)

        # Spellchecking
        spellingCorrectionDetailsSentences = []
        spellingCorrectionDetailsWords = []
        spellingCorrectionDetailsSuggestions = []
        spellingCorrectionDetailsChosenSuggestion = []
        spellingCorrectionDetailsChangesWord = []
        spellingCorrectionDetailsReplacementLength = []
        spellingCorrectionCount = 0

        spellchecker = enchant.DictWithPWL(spellcheckerLibrary, pwl = exclusionsFileFullPath, broker = b)
        chkr = SpellChecker(spellchecker, sentence, filters = [EmailFilter, URLFilter])

        collectMisspellingDetails = {
            'Word': [], 
            'Substitution': [], 
            'SubstitutionText': []
            }

        for err in chkr:

            #print('\nSpellcheck Word:', err.word)
            matchedWord = False

            word = err.word

            if lexicons is not None and provideMisspellingDetailed:

                appendLexiconLabel = ''

                for lexicon, tagTokenPairs in lexicons.items():

                    lexiconName = '|_|' + lexicon.upper() + '&'

                    matchedWord = False  # note: we want to capture in multiple lexicons (but only once per lexicon)

                    for tag, tokens in tagTokenPairs.items():

                        if matchedWord:
                            break

                        elif any('*' in s for s in tokens):
                            # regex mode
                            nonmatching = [s for s in tokens if not s.endswith('*')]
                            if word.lower() in nonmatching:
                                appendLexiconLabel += lexiconName + tag.upper()
                                matchedWord = True
                            else:
                                matching = [s for s in tokens if s.endswith('*')]
                                for eachToken in matching:
                                    startString = eachToken[:-1]
                                    startStringUnique = set(startString)
                                    if startStringUnique != set('*'):
                                        if word.lower().startswith(startString):

                                            appendLexiconLabel += lexiconName + tag.upper()
                                            matchedWord = True
                                    else:
                                        if eachToken == word.lower():

                                            appendLexiconLabel += lexiconName + tag.upper()
                                            matchedWord = True

                        elif word.lower() in tokens:

                            appendLexiconLabel += lexiconName + tag.upper()
                            matchedWord = True

                collectMisspellingDetails['SubstitutionText'].append('MISSPELLING' + appendLexiconLabel)

            #print(appendLexiconLabel)
            collectMisspellingDetails['Word'].append(err.word)
            collectMisspellingDetails['Substitution'].append('ABCMISSPELLING' + str(len(collectMisspellingDetails['Word'])) + 'XYZ')

            if (len(err.suggest()) == 0):
                spellingCorrectionDetailsSentences.append(sentence)
                spellingCorrectionDetailsChangesWord.append('True')
                spellingCorrectionDetailsWords.append(err.word)
                spellingCorrectionDetailsSuggestions.append(' | '.join(err.suggest()))
                spellingCorrectionDetailsChosenSuggestion.append('NA')
                spellingCorrectionDetailsReplacementLength.append('NA')
            else: # no need to count case corrections (e.g., i'm = I'm), but go ahead and perform them
                spellingCorrectionDetailsSentences.append(sentence)
                spellingCorrectionDetailsWords.append(err.word)
                spellingCorrectionDetailsSuggestions.append(' | '.join(err.suggest()))
                if err.word.lower() != err.suggest()[0].lower():
                    spellingCorrectionDetailsChangesWord.append('True')
                    spellingCorrectionCount += 1
                else:
                    spellingCorrectionDetailsChangesWord.append('False')

                finalSuggestions = err.suggest()

                err.replace(finalSuggestions[0])
                spellingCorrectionDetailsChosenSuggestion.append(finalSuggestions[0])
                spellingCorrectionDetailsReplacementLength.append(len(finalSuggestions[0].split()))

        sentenceMisspelling = sentence
        #print('\nRaw:', sentenceMisspelling)

        for i, word in enumerate(collectMisspellingDetails['Word']):

            replacementLength = spellingCorrectionDetailsReplacementLength[i]
            # if there is no suggested replacement
            if replacementLength == 'NA':
                replacementLength = 1

            sentenceMisspelling = re.sub('(?<=[^a-zA-Z0-9])' + word + '(?![a-zA-Z0-9])', ' '.join([collectMisspellingDetails['Substitution'][i]] * replacementLength), sentenceMisspelling, count = 1)

        MisspellingRaw = ' '.join(spaCyTOK(sentenceMisspelling)).lower()

        Misspelling = re.sub('ABCMISSPELLING[0-9]+XYZ'.lower(), 'MISSPELLING', MisspellingRaw)

        if provideMisspellingDetailed == True:

            MisspellingDetailed = MisspellingRaw

            for i, word in enumerate(collectMisspellingDetails['Word']):

                replacementLength = spellingCorrectionDetailsReplacementLength[i]
                # if there is no suggested replacement
                if replacementLength == 'NA':
                    replacementLength = 1

                MisspellingDetailed = MisspellingDetailed.replace(collectMisspellingDetails['Substitution'][i].lower(), collectMisspellingDetails['SubstitutionText'][i], replacementLength)


            MisspellingDetailed = MisspellingDetailed

        #print('\nMISSPELLING Representation:', Misspelling)
        #print('\nMISSPELLINGDETAILED Representation:', MisspellingDetailed)

        if useSpellChecker:
            sentence = chkr.get_text()
            correctedSentence = sentence
        else:
            correctedSentence = chkr.get_text()

        #print('\nCorrected Sentence:', correctedSentence)

        checkLength = [
            len(spellingCorrectionDetailsSentences),
            len(spellingCorrectionDetailsWords),
            len(spellingCorrectionDetailsChangesWord),
            len(spellingCorrectionDetailsReplacementLength),
            len(spellingCorrectionDetailsSuggestions),
            len(spellingCorrectionDetailsChosenSuggestion)
            ]

        if debug:
            print('correctionDF:', checkLength)

        if not all(x == checkLength[0] for x in checkLength):
            print('\nProblem detected with the following text (spellchecker):', '\n')
            print(sentence)
            print(spellingCorrectionDetailsSuggestions)
            print(spellingCorrectionDetailsChosenSuggestion)
            print(spellingCorrectionDetailsReplacementLength)

        correctionDF = pd.DataFrame({
            #'RawInput': spellingCorrectionDetailsSentences,
            'RawWord': spellingCorrectionDetailsWords,
            'ChangesWord': spellingCorrectionDetailsChangesWord,
            'ReplacementLength': spellingCorrectionDetailsReplacementLength,
            'Suggestions': spellingCorrectionDetailsSuggestions,
            'ChosenSuggestion': spellingCorrectionDetailsChosenSuggestion
            })

        if debug:
            print('CorrectedSentence:', correctedSentence)
            print('CountStrippedWhitespaceChars:', whitespaceStripLength)
            print('CountStrippedHTMLChars:', htmlStripLength)
            print('CountSpellingCorrections', spellingCorrectionCount)
            print(correctionDF)

        resReturn = pd.DataFrame({
            'Sentence': sentence, 
            'Feature_Misspelling': Misspelling,
            'Spellchecker_CorrectedSentence': correctedSentence,
            'Spellchecker_CountStrippedWhitespaceChars': whitespaceStripLength,
            'Spellchecker_CountStrippedHTMLChars': htmlStripLength,
            'Spellchecker_CountSpellingCorrections': spellingCorrectionCount
            }, index = [0])

        if provideMisspellingDetailed:
            resReturn['Feature_MisspellingDetailed'] = MisspellingDetailed

        return([resReturn, correctionDF])

    # Basic Text Cleanup
    print('# Performing Basic Text Cleanup #\n')
    res = textData['InitialSentence'].mapply(BasicTextCleanup, debug = debug)
    resZip = list(zip(*res))

    textData = pd.concat([textData, pd.concat(resZip[0], ignore_index = True)], axis = 1)
    corrections = pd.concat(resZip[1], ignore_index = True)
    
    # Process Text with spaCy
    print('\n# Processing Text Representations #\n')
    def ProcessText (doc, debug = debug):

        doc = nlp(doc)

        all_word = []
        all_word_lower = []
        all_pos = []
        all_word_pos = []
        all_ner = []
        all_word_ner = []
        all_bounds = []

        for token in doc:

            word = token.text
            pos = token.pos_

            all_word.append(word)
            all_word_lower.append(token.lower_)
            all_pos.append(pos)
            all_word_pos.append(token.lower_ + '|_|' + pos)

            if token.ent_iob_ == "O":
                ner = token.lower_
                all_word_ner.append(token.lower_)
            else:
                ner = token.ent_type_
                all_word_ner.append(token.lower_ + '|_|' + token.ent_type_)

            all_ner.append(ner)

        sents = doc.sents

        for eachSent in sents:
            sentBounds = ['-'] * len([token.text for token in eachSent])
            sentBounds[-1] = 'S'
            all_bounds += sentBounds

        all_bounds = np.array(all_bounds)
        all_bounds[np.where(np.array(all_word) == '|||')] = 'D'

        # Vars
        Word        = all_word_lower
        POS         = all_pos
        Word_POS    = all_word_pos
        NER         = all_ner
        Word_NER    = all_word_ner
        Boundaries  = all_bounds

        # Word Sense Disambiguation
        tempWS = disambiguate(' '.join(all_word), algorithm = adapted_lesk, tokenizer = splitWS)
        tempWSRaw = [x[1] for x in tempWS]

        # Hypernym, Sentiment, Affect
        Hypernym = []
        Sentiment = []
        Affect = []
        Word_Sense = []

        # for WNAffect
        POSTreeBank = nltk.pos_tag(all_word)

        for i, each in enumerate(Word):

            try:
                wnaRes = str(wna.get_emotion(Word[i], POSTreeBank[i][1]).get_level(wnaReturnLevel))
                Affect.append(wnaRes.upper())
            except:
                Affect.append(Word[i])

            if (str(tempWSRaw[i]) != 'None'):

                Word_Sense.append(Word[i] + '|_|' + tempWS[i][1].name().split('.')[-1:][0])

                hypernyms = tempWS[i][1].hypernyms()

                if len(hypernyms) > 0:
                    Hypernym.append(hypernyms[0].name().split('.')[0].upper())
                else:
                    Hypernym.append(Word[i])

                swnScores = swn.senti_synset(tempWS[i][1].name())

                wordSentiment = ''

                if swnScores.pos_score() > 2/3:
                    wordSentiment += 'HPOS'
                elif swnScores.pos_score() > 1/3:
                    wordSentiment += 'MPOS'
                else:
                    wordSentiment += 'LPOS'

                if swnScores.neg_score() > 2/3:
                    wordSentiment += 'HNEG'
                elif swnScores.neg_score() > 1/3:
                    wordSentiment += 'MNEG'
                else:
                    wordSentiment += 'LNEG'

                Sentiment.append(wordSentiment)

            else:
                Word_Sense.append(Word[i])
                Hypernym.append(Word[i])
                Sentiment.append(Word[i])

        res = {
            'Feature_Word': all_word_lower,
            'Feature_POS': all_pos,
            'Feature_Word&POS': all_word_pos,
            'Feature_NER': all_ner,
            'Feature_Word&NER': all_word_ner,
            'Feature_Boundaries': all_bounds,
            'Feature_Affect': Affect,
            'Feature_Word&Sense': Word_Sense,
            'Feature_Hypernym': Hypernym,
            'Feature_Sentiment': Sentiment,
            }
        
        # Generate separate lexicon features (if available)
        LexiconFeatures = {}

        if lexicons is not None:

            for lexicon, tagTokenPairs in lexicons.items():

                lexiconName = 'Feature_Lexicon' + lexicon.upper()
                LexiconFeatures[lexiconName] = []

                for i, word in enumerate(Word):

                    LexiconFeatures[lexiconName].append(word)
                    wordReplaced = False

                    for tag, tokens in tagTokenPairs.items():
                        if wordReplaced:
                            break
                        elif any('*' in s for s in tokens):
                            # regex mode
                            nonmatching = [s for s in tokens if not s.endswith('*')]
                            if word.lower() in nonmatching:
                                LexiconFeatures[lexiconName][i] = tag.upper()
                                wordReplaced = True
                            else:
                                matching = [s for s in tokens if s.endswith('*')]
                                for eachToken in matching:
                                    startString = eachToken[:-1]
                                    startStringUnique = set(startString)
                                    if startStringUnique != set('*'):
                                        if word.lower().startswith(startString):
                                            LexiconFeatures[lexiconName][i] = tag.upper()
                                            matchedWord = True
                                    else:
                                        if eachToken == word.lower():
                                            LexiconFeatures[lexiconName][i] = tag.upper()
                                            matchedWord = True

                        elif word.lower() in tokens:

                            LexiconFeatures[lexiconName][i] = tag.upper()
                            wordReplaced = True

        if lexicons is not None:
            res.update(LexiconFeatures)

        checkLength = [len(res[each]) for each in res]

        if len(set(checkLength)) != 1:
            print('Check Length:', checkLength)
            print('Problem detected with the following text:')
            print(sentence)

        # Rejoin features
        for each in res.keys():
            res[each] = ' '.join(res[each])

        return(res)

    res = textData['Sentence'].mapply(ProcessText)
    textData = pd.concat([textData, pd.DataFrame(res.values.tolist())], axis = 1)

    return([textData, corrections])






