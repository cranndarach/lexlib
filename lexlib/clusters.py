#!/usr/bin/env python3

"""
Functions for dealing with consonant clusters.
"""

# module: clusters
# copyright: 2016-2018 R. Steiner
# license: MIT License

import itertools as it


def clusters(words, vowels, sep=None, unique=False, case_sensitive=True):
    """
    Separates a list of *words* into clusters. Clusters are defined as
    sequences of characters that do not contain any of the characters
    in the list of *vowels*.

    If *sep* is defined, it will be used as the delimiter string (for
    example, with `sep="."`, the word "a.bc.de" will be treated as the
    three-character sequence `["a", "bc", "de"]`).

    If *unique* is `True`, returns each cluster only once. If *unique*
    is `False` (the default), returns each cluster as many times as it
    occurs.

    If *case_sensitive* is `True` (the default), uppercase and lowercase
    characters will be treated as two different characters (e.g., "a"
    will be seen as different from "A"). If *case_sensitive* is `False`,
    uppercase and lowercase characters will be treated as the same
    character, and the output will be lowercase (e.g., "a" and "A" will
    both be treated as "a").
    """
    if unique not in [True, False]:
        raise AttributeError("'unique' must be either True or False.")
    if case_sensitive not in [True, False]:
        raise AttributeError("'case_sensitive' must be either True or False.")
    clusts = [clusters_word(word, vowels, sep) for word in words]
    flattened = list(it.chain(*clusts))
    if unique:
        output = list(set(flattened))
    else:
        output = flattened
    return output


def clusters_word(word, vowels, sep=None, case_sensitive=True):
    """
    Separates a *word* into clusters, defined as sequences of
    characters that do not contain any of the characters in the list of
    *vowels*.

    If *sep* is defined, it will be used as the delimiter string (for
    example, with `sep="."`, the word "a.bc.de" will be treated as the
    three-character sequence `["a", "bc", "de"]`).

    If *case_sensitive* is `True` (the default), uppercase and lowercase
    characters will be treated as two different characters (e.g., "a"
    will be seen as different from "A"). If *case_sensitive* is `False`,
    uppercase and lowercase characters will be treated as the same
    character, and the output will be lowercase (e.g., "a" and "A" will
    both be treated as "a").
    """
    if case_sensitive not in [True, False]:
        raise AttributeError("'case_sensitive' must be either True or False.")
    if not case_sensitive:
        word = word.lower()
        vowels = [v.lower() for v in vowels]
    output = []
    wkspc = []
    word = list(word) if not sep else word.split(sep)
    for char in word:
        # If char is a vowel and wkspc is non-empty, add cluster to list.
        if char in vowels and wkspc:
            output.append(__finalize_cluster(wkspc, sep))
            wkspc = []
        # If char is a vowel and wkspc is empty, move on.
        elif char in vowels and not wkspc:
            continue
        # If char is not a vowel, add it to the working cluster.
        else:
            wkspc.append(char)
    else:
        if wkspc:
            output += __finalize_cluster(wkspc, sep)
        else:
            None
    return output


def __finalize_cluster(chars, sep):
    if sep:
        cluster = sep.join(chars)
    else:
        cluster = "".join(chars)
    return cluster
