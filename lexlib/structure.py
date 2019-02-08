#!/usr/bin/env python3

"""
Functions related to the structure of words.
"""

# module: structure
# copyright: 2019 R. Steiner
# license: MIT License


def get_cv(word, vowels, sep=None):
    """
    Calculate the consonant ("C") and vowel ("V") structure of the
    given word. Returns a string of the characters "C" and "V"
    corresponding to the characters in the word.

    *vowels* -- A list of the characters representing vowels.

    *sep* -- String used to separate phonemes (if the words are
    phonological forms). To separate into individual characters, set to
    `None` (default).
    """
    wsplit = list(word) if not sep else word.split(sep)
    pattern = ["C" if char not in vowels else "V" for char in wsplit]
    return "".join(pattern)
