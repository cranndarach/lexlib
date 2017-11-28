#!/usr/bin/env python3

"""
|  module: lexlib
|  author: R. Steiner
|  license: MIT License copyright (c) 2016, 2017 R. Steiner
|  description: Set of utilities for research involving words.
"""

import csv
import warnings

__all__ = ["get_words", "clusters", "get_neighbor_dict", "get_neighbor_pairs",
           "get_neighbor_positions", "get_neighbor_types", "get_neighbors",
           "nsyll_word", "nsyll_list", "filter_by_nsyll", "filter_words"]


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
# Neighbors #
#############


def get_neighbor_dict(words, **kwargs):
    """
    Compare each word in a list of *words* to each word in a *corpus* word list
    (or in the same list if *corpus* is not given), and return a dict where
    each target word is a key, and its value is a list of its neighbors. (If you
    are looking for a function to get neighbor pairs, see `get_neighbor_pairs()`).

    keyword arguments:
        *corpus* -- List of all the words to get the neighbors from. If empty,
        defaults to `words`.

        *sep* -- String used to separate phonemes (if the words are phonological
        forms). To separate into individual characters, set to `None` (default).

        *debug* -- If True, it logs the current word and the words being
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
    Compare each word in a list of *words* to each word in a *corpus* word list
    (or in the same list if *corpus* is not given), and return a list of `(word,
    neighbor)` pairs. (If you are looking for a function to get lists of all
    the neighbors for specific words, see `get_neighbor_pairs()`).

    keyword arguments:
        *corpus* -- List of all the words to get the neighbors from. If empty,
        defaults to `words`.

        *sep* -- String used to separate phonemes (if the words are phonological
        forms).  To separate into individual characters, set to `None` (default).

        *debug* -- If True, it logs the current word and the words being
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


def get_neighbor_positions(neighbor_pairs):
    """
    Given a list of `(word1, word2)` *neighbor_pairs*, return a list of
    `(word1, word2, position)` triples, where `position` is the position in the
    words where the neighbor relationship is formed. Note that this can only
    be calculated for pairs of substitution neighbors. If the words differ in
    length, `position` will be `-1`.

    Example:
        ```
        >>> neighbor_pairs = [("cat", "cap"), ("cat", "cut"), ("cat", "cast")]
        >>> get_neighbor_positions(neighbor_pairs)
        [("cat", "cap", 3), ("cat", "cut", 2), ("cat", "cast", -1)]
        ```
    """
    return [__get_position(neighbors) for neighbors in neighbor_pairs]


def get_neighbor_types(neighbor_dict):
    """
    Given a *neighbor_dict* (where a key is a "target" word and its value is a
    list of all of its neighbors), return a list of `(word1, word2, relationship)`
    triples, where `relationship` is one of "deletion,"
    "addition," "substitution," or "unknown".
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


def __get_position(neighbors):
    first, second = neighbors
    if len(first) != len(second):
        return (first, second, -1)
    for pos in range(len(first)):
        if first[pos] != second[pos]:
            return (first, second, pos+1)
    else:
        return (first, second, 0)


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
