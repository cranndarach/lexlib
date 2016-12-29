#!/usr/bin/env python3

"""module: syllable_filter
author: R Steiner
license: MIT, copyright (c) 2016 R Steiner
description: Functions to filter words with desired number of syllables
from a corpus.
"""


def __decorator(fnc):
    return fnc


def __load_file(filepath):
    with open(filepath, 'r') as f:
        corpus = [word[:-1] for word in f]
    return corpus

load_corpus = __decorator(__load_file)
load_vowels = __decorator(__load_file)


def __count_syllables(word, vowels, sep=None):
    """
    Returns the number of syllables (vowels) in a word.

    Arguments:
    word -- the word to be analyzed
    """
    counter = 0
    phonemes = list(word) if not sep else word.split(sep)
    for phoneme in phonemes:
        counter += 1 if phoneme in vowels else 0
    return counter


def filter_words(corpus, vowels, nsyll, sep=None):
    """
    Returns a list of the words with the desired number of syllables.

    Arguments:
    corpus -- list of words to filter.
    vowels -- a list of the vowels used in the corpus.
    nsyll -- an integer or list of integers containing the number of
    syllables desired.
    sep -- string to use as the delimiter for separating phonemes in the
    words in the corpus. default: None (separate into individual characters)
    """
    nsyll = [nsyll] if type(nsyll) == int else nsyll
    match = list(filter(lambda w: __count_syllables(w) in nsyll, corpus))
    return match
