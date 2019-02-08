#!/usr/bin/env python3

"""
Functions related to the structure of words.
"""

# module: structure
# copyright: 2016-2019 R. Steiner
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


def __finalize_cluster(chars, sep):
    if sep:
        cluster = sep.join(chars)
    else:
        cluster = "".join(chars)
    return cluster


def __is_desired_nsyll(word, vowels, sep, nsyll):
    """
    Where nsyll is a list of desired syllable lengths. Return True if
    the word's syllable count is in the list of desired lengths; else,
    return False.
    """
    return nsyll_word(word, vowels, sep) in nsyll
