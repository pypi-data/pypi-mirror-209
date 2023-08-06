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

def ReadAllLexicons (lexiconFileFullPath):

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







