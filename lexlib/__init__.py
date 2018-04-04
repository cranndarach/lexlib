#!/usr/bin/env python3

"""
|  module: lexlib
|  author: R. Steiner
|  license: MIT License copyright (c) 2016, 2017 R. Steiner
|  description: Set of utilities for research involving words.
"""

import csv
import warnings

from .neighbors import *

__all__ = ["check_neighbors", "get_words", "clusters", "get_neighbor_dict",
           "get_neighbor_pairs", "get_neighbor_positions",
           "get_neighbor_types", "get_neighbors", "nsyll_word", "nsyll_list",
           "filter_by_nsyll", "filter_words"]


#######
# I/O #
#######


def get_words(file_path, column_name, delimiter=",", **fmtparams):
    """
    Return a list containing only the items from the *column_name* column in
    the *delimiter*-separated file found at *file_path*. Also takes any
    of `csv.DictReader`'s *fmtparams*.
    """
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter, **fmtparams)
        words = [row[column_name] for row in reader]
    return words


############
# Clusters #
############


def clusters(words, vowels, sep=None):
    """
    Separates a list of *words* into clusters. Clusters are defined as sequences
    of characters that do not contain any of the characters in the list of
    *vowels*.

    If *sep* is defined, it will be used as the delimiter string (for example,
    with `sep="."`, the word "a.bc.de" will be treated as the three-character
    sequence `["a", "bc", "de"]`).
    """
    output = []
    for word in words:
        output.extend(__segment(word, vowels, sep))
    return output


def __segment(word, vowels, sep):
    output = []
    wkspc = ""
    word = list(word) if not sep else word.split(sep)
    # word = word.split(sep)
    for char in word:
        char = char.lower()
        if char in vowels:
            output.append(wkspc) if wkspc != "" else None
            wkspc = ""
        else:
            wkspc += char
    else:
        output.append(wkspc) if wkspc != "" else None
    return output


#############
# Syllables #
#############


def nsyll_word(word, vowels, sep=None):
    """
    Count the number of syllables in a *word*, determined by the number of
    characters from the *vowels* list found in that word.

    If *sep* is defined, it will be used as the delimiter string (for example,
    with `sep="."`, the word "a.bc.de" will be treated as the three-character
    sequence `["a", "bc", "de"]`).
    """
    counter = 0
    # This actually makes it safe to use '' as the delimiter, because that will
    # make `if not sep` return True.
    phonemes = list(word) if not sep else word.split(sep)
    for phoneme in phonemes:
        counter += 1 if phoneme in vowels else 0
    return counter


def nsyll_list(words, vowels, sep=None):
    """
    Count the number of syllables in each word in a *words* list, determined by
    the number of characters from the *vowels* list found in that word. Return a
    list of `(word, nsyll)` pairs.

    If *sep* is defined, it will be used as the delimiter string (for example,
    with `sep="."`, the word "a.bc.de" will be treated as the three-character
    sequence `["a", "bc", "de"]`).
    """
    output = []
    for w in words:
        nsyll = nsyll_word(w, vowels, sep)
        output.append((w, nsyll))
    return output


def filter_by_nsyll(words, vowels, nsyll, sep=None):
    """
    Given a list of *words*, return a list containing only the words with the
    desired number of syllables, determined by the number of characters from the
    *vowels* list found in that word.

    The number of syllables, *nsyll* can be
    either an integer or a list of integers. If it is a list, the returned list
    will contain words of any syllable length included in *nsyll*.

    If *sep* is defined, it will be used as the delimiter string (for example,
    with `sep="."`, the word "a.bc.de" will be treated as the three-character
    sequence `["a", "bc", "de"]`).
    """
    nsyll = [nsyll] if type(nsyll) == int else nsyll
    match = list(filter(lambda w: __is_desired_nsyll(w, vowels, sep, nsyll), words))
    return match


def __is_desired_nsyll(word, vowels, sep, nsyll):
    """
    Where nsyll is a list of desired syllable lengths. Return True if the word's
    syllable count is in the list of desired lengths; else, return False.
    """
    return nsyll_word(word, vowels, sep) in nsyll


#############
# Utilities #
#############


def deprecation_decorator(func):
    def wrapper(*args, **kwargs):
        msg = "Please use '{}' instead".format(func.__name__)
        warnings.warn(msg, DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper

get_neighbors = deprecation_decorator(get_neighbor_dict)
filter_words = deprecation_decorator(filter_by_nsyll)
