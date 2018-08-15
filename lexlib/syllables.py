#!/usr/bin/env python3

"""
Functions for working with syllables.
"""

# module: syllables
# copyright: 2016-2018 R. Steiner
# license: MIT License


def nsyll_word(word, vowels, sep=None):
    """
    Count the number of syllables in a *word*, determined by the number
    of characters from the *vowels* list found in that word.

    If *sep* is defined, it will be used as the delimiter string (for
    example, with `sep="."`, the word "a.bc.de" will be treated as the
    three-character sequence `["a", "bc", "de"]`).
    """
    counter = 0
    # This actually makes it safe to use '' as the delimiter, because that
    # will make `if not sep` return True.
    phonemes = list(word) if not sep else word.split(sep)
    for phoneme in phonemes:
        counter += 1 if phoneme in vowels else 0
    return counter


def nsyll_list(words, vowels, sep=None):
    """
    Count the number of syllables in each word in a *words* list,
    determined by the number of characters from the *vowels* list found
    in that word. Return a list of `(word, nsyll)` pairs.

    If *sep* is defined, it will be used as the delimiter string (for
    example, with `sep="."`, the word "a.bc.de" will be treated as the
    three-character sequence `["a", "bc", "de"]`).
    """
    return [nsyll_word(w, vowels, sep) for w in words]


def filter_by_nsyll(words, vowels, nsyll, sep=None):
    """
    Given a list of *words*, return a list containing only the words
    with the desired number of syllables, determined by the number of
    characters from the *vowels* list found in that word.

    The number of syllables, *nsyll* can be either an integer or a list
    of integers. If it is a list, the returned list will contain words
    of any syllable length included in *nsyll*.

    If *sep* is defined, it will be used as the delimiter string (for
    example, with `sep="."`, the word "a.bc.de" will be treated as the
    three-character sequence `["a", "bc", "de"]`).
    """
    nsyll = [nsyll] if type(nsyll) == int else nsyll
    match = list(filter(lambda w: __is_desired_nsyll(w, vowels, sep, nsyll),
                        words))
    return match


def __is_desired_nsyll(word, vowels, sep, nsyll):
    """
    Where nsyll is a list of desired syllable lengths. Return True if
    the word's syllable count is in the list of desired lengths; else,
    return False.
    """
    return nsyll_word(word, vowels, sep) in nsyll
