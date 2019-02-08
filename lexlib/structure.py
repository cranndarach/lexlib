#!/usr/bin/env python3

"""
Functions related to the structure of words.
"""

# module: structure
# copyright: 2019 R. Steiner
# license: MIT License


def get_cv(word, vowels, sep=None):
    wsplit = list(word) if not sep else word.split(sep)
    pattern = ["C" if char not in vowels else "V" for char in wsplit]
    return "".join(pattern)
