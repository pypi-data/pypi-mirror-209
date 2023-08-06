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

import warnings
warnings.filterwarnings('ignore', message = '.*looks like a URL.*', category = UserWarning, module = 'bs4')

def say_hello():
    print("Hello, World!")

### Read Custom Lexicons Function: ###
def ReadAllLexicons (lexiconpath, lexiconFileFullPath = False):

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

    if lexiconFileFullPath:
        
        if lexiconFileFullPath != 'None':

            zipFile = zf.ZipFile(lexiconFileFullPath, 'r')
            for file in sorted(zipFile.namelist()):
                if fnmatch.fnmatch(file, '*.txt'):
                    L = zipFile.read(file).decode('utf-8').encode('utf-8').decode('unicode-escape')
                    customLexicons = BuildLexicon(L, customLexicons)
    else:

        for (dir, dirs, files) in os.walk(lexiconpath):
            for file in files:
                if fnmatch.fnmatch(file, '*.txt'):
                    L = open(os.path.join(dir, file), "r").read().encode('utf-8').decode('unicode-escape')
                    #L = codecs.open(os.path.join(dir, file), "r", "utf-8").read()
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