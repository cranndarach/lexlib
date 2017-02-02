#!/usr/bin/env python3

"""
module: cluster.py
author: R Steiner
license: MIT License copyright (c) 2016 R Steiner
description: Separate a list of words into clusters.
"""


def clusters(words, vowels, sep=None):
    """
    Separates a list of words into clusters, defined as sequences of
    characters that do not contain a vowel.

    Keyword arguments:
    words -- a list of the word forms to serve as the source for clusters
    vowels -- a list of vowels
    sep -- string that separates phonemes/letters/segments. default: "" (empty
    string)
    """
    output = []
    for word in words:
        output.extend(__segment(word, vowels, sep))
    return output


def positional_clusters(words, vowels, sep=None):
    """
    Separate clusters into those that occur at the start of a word,
    those that occur at the end of a word, and the rest. Returns a
    triple of lists of strings: (initial, medial, final)

    Keyword arguments:
    words -- a list of the word forms to serve as the source for clusters
    vowels -- a list of vowels
    sep -- string that separates phonemes/letters/segments. default: "" (empty
    string)
    """
    initial = []
    medial = []
    final = []
    for word in words:
        clusters = __segment(word, vowels, sep)
        initial.append(clusters.pop(0))
        if clusters:
            final.append(clusters.pop(-1))
        if clusters:
            medial.extend(clusters)
    return initial, medial, final


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
