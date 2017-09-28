#!/usr/bin/env python3

"""
module: lexlib
author: R. Steiner
license: MIT License copyright (c) 2016, 2017 R. Steiner
description: Set of utilities for research involving words.
"""

import csv
import warnings

__all__ = ["get_words", "clusters", "get_neighbor_dict",
           "get_neighbor_pairs", "get_neighbors", "nsyll_word", "nsyll_list",
           "filter_by_nsyll", "filter_words"]


#######
# I/O #
#######


def get_words(file_path, column_name, delimiter=",", **fmtparams):
    """
    Returns a list containing only the specified column.

    arguments:
    file_path -- path to the file containing the corpus (a CSV or tab-separated
    text file, etc.).
    column_name -- the name of the column in the given file that contains the words.
    delimiter -- the string separating the cells in the database. Default: ","
    **fmtparams -- any additional formatting arguments for the built-in
    `csv.DictReader` function.
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
# Neighbors #
#############


def get_neighbor_dict(words, **kwargs):
    """
    Compares each word in a target list to each word in a corpus (or in the same
    list if `corpus` is not given), and returns a dict where each target word is
    a key, and its value is a list of its neighbors. (If you are looking for a
    function to get neighbor pairs, see get_neighbor_pairs()).

    positional arguments:
        words -- List of words whose neighbors will be found.

    keyword arguments:
        corpus -- List of all the words to get the neighbors from. If empty,
        defaults to `words`.
        sep -- String used to separate phonemes (if the words are phonological
        forms).  To separate into individual characters, set to `None` (default).
        debug -- If True, it logs the current word and the words being
        compared to it to the console. Defaults to False.
    """
    sep = kwargs.get("sep", None)
    debug = kwargs.get("debug", None)
    corpus = kwargs.get("corpus", words)
    neighbors = []
    neighbors = {}
    # for word in words:
    while words:
        word = words.pop()
        print(word) if debug else None
        neighbors[word] = []
        wsplit = list(word) if not sep else word.split(sep)
        wlen = len(wsplit)
        for q in corpus:
            print("\t", q) if debug else None
            qsplit = list(q) if not sep else q.split(sep)
            if len(qsplit) == wlen:
                neighbors[word].append(q) if __check_substitution(wsplit, qsplit) else None
            elif len(qsplit) == wlen+1:
                neighbors[word].append(q) if __check_addition(wsplit, qsplit) else None
            elif len(qsplit) == wlen-1:
                neighbors[word].append(q) if __check_deletion(wsplit, qsplit) else None
            else:
                continue
    return neighbors


def get_neighbor_pairs(words, **kwargs):
    """
    Compares each word in a target list to each word in a corpus (or in the same
    list if `corpus` is not given), and returns a dict where each target word is
    a key, and its value is a list of its neighbors. (If you are looking for a
    function to get lists of all the neighbors for specific words, see
    get_neighbor_pairs()).

    positional arguments:
        words -- List of words whose neighbors will be found.

    keyword arguments:
        corpus -- List of all the words to get the neighbors from. If empty,
        defaults to `words`.
        sep -- String used to separate phonemes (if the words are phonological
        forms).  To separate into individual characters, set to `None` (default).
        debug -- If True, it logs the current word and the words being
        compared to it to the console. Defaults to False.
    """
    sep = kwargs.get("sep", None)
    debug = kwargs.get("debug", None)
    corpus = kwargs.get("corpus", words)
    neighbors = []
    while words:
        word = words.pop()
        print(word) if debug else None
        # Lighten the memory load and avoid duplicates.
        if word in corpus:
            corpus.remove(word)
        wsplit = list(word) if not sep else word.split(sep)
        wlen = len(wsplit)
        for q in corpus:
            print("\t", q) if debug else None
            qsplit = list(q) if not sep else q.split(sep)
            if len(qsplit) == wlen:
                neighbors.append((word, q)) if __check_substitution(wsplit, qsplit) else None
            elif len(qsplit) == wlen+1:
                neighbors.append((word, q)) if __check_addition(wsplit, qsplit) else None
            elif len(qsplit) == wlen-1:
                neighbors.append((word, q)) if __check_deletion(wsplit, qsplit) else None
            else:
                continue
    return neighbors


def get_neighbor_types(neighbor_dict):
    """
    Takes a dict of neighbors (where a key is a "target" word and its value is a
    list of all of its neighbors) and returns a list of (word1, word2,
    relationship) triples, where `relationship` is one of "deletion,"
    "addition," "substitution," or "unknown".

    arguments:
        neighbor_dict -- a dict whose keys are target words, and their values are
        a list of their neighbors (e.g., the output of get_neighbor_dict()).
    """
    types = []
    targets = neighbor_dict.keys()
    while targets:
        current = targets.pop()
        for neighbor in neighbor_dict[current]:
            if len(current) == len(neighbor): # if they are the same length, the change was a substitution
                types.append((current, neighbor, "substitution"))
            elif len(current) > len(neighbor): # if the target is longer than the neighbor, the change was a deletion
                types.append((current, neighbor, "deletion"))
            elif len(current) < len(neighbor): # if the target is shorter than the neighbor, the change was an addition
                types.append((current, neighbor, "addition"))
            else: # just to be sure
                types.append((current, neighbor, "unknown"))
    return types


def __check_addition(base, candidate):
    strikes = 0
    for position in range(len(base)):
        while True:
            # If they match, break the while loop and try the next position.
            if base[position] == candidate[position+strikes]:
                break
            # Otherwise, take a strike and continue on that position,
            # as long as it's the first strike. If it's the second strike,
            # then they are not neighbors, so return False.
            else:
                strikes += 1
                if strikes >= 2:
                    return False
    else:
        return True


def __check_deletion(base, candidate):
    strikes = 0
    for position in range(len(candidate)):
        while True:
            if base[position+strikes] == candidate[position]:
                break
            else:
                strikes += 1
                if strikes >= 2:
                    return False
    else:
        return True


def __check_substitution(base, candidate):
    strikes = 0
    for position in range(len(base)):
        if base[position] == candidate[position]:
            continue
        else:
            strikes += 1
            if strikes >= 2:
                return False
    else:
        return True


#############
# Syllables #
#############


def nsyll_word(word, vowels, sep=None):
    """
    Returns the number of syllables (vowels) in a word.

    Arguments:
    word -- the word to be analyzed
    vowels -- a list of vowels used in the word list's alphabet.
    sep -- string to use as the delimiter for separating phonemes in the
    words in the list. default: None (separate into individual characters)
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
    Counts the number of syllables in each word for a list of words. Returns a
    list of (word, nsyll) pairs.

    Arguments:
    words -- a list of words whose syllables will be counted.
    vowels -- a list of vowels used in the word list's alphabet.
    sep -- string to use as the delimiter for separating phonemes in the
    words in the list. default: None (separate into individual characters)
    """
    output = []
    for w in words:
        nsyll = nsyll_word(w, vowels, sep)
        output.append((w, nsyll))
    return output


def filter_by_nsyll(corpus, vowels, nsyll, sep=None):
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
    match = list(filter(lambda w: __is_desired_nsyll(w, vowels, sep, nsyll), corpus))
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

# deprecated = {
#     "get_neighbors": {
#         "alternative": get_neighbor_dict(),
#         "note": "Or, see the new function `get_neighbor_pairs()`."
#         },
#     "filter_words": {"alternative": filter_by_nsyll()}
#     }


def deprecation_decorator(func):
    def wrapper(*args, **kwargs):
        msg = "Please use '{}' instead".format(func.__name__)
        warnings.warn(msg, DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper

get_neighbors = deprecation_decorator(get_neighbor_dict)
filter_words = deprecation_decorator(filter_by_nsyll)
