#!/usr/bin/env python3

"""
module: get_neighbor.py
author: R Steiner
license: MIT License, copyright (c) 2016 R Steiner
description: Functions to find the phonological neighbors of a list of words.
"""

import pandas as pd


def get_neighbor_dict(words, corpus, sep=None, debug=False):
    """
    Iterates through the word list, comparing each word in the
    corpus to the current word in length, and passing it to the
    appropriate "checker" function, or moving on if its length
    indicates that it is not a neighbor. If the checker returns
    True, then it appends that word to the current word's "neighbor"
    entry.

    keyword arguments:
        words -- List of words whose neighbors will be found.
        corpus -- List of all the words to get the neighbors from. If empty,
        defaults to `words`.
        sep -- String used to separate phonemes (if the words are phonological
        forms).  To separate into individual characters, set to `None` (default).
        debug -- If True, it logs the current word and the words being
        compared to it to the console. Defaults to False.
    """
    neighbors = {}
    for word in words:
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
    (To be documented further, but briefly:)
    Get a list of pairs of neighbors. Alternative to get_neighbor_dict(), which
    returns a dict with an entry for each word, and a list of its neighbors.
    This is preferable when you want to calculate over pairs themselves or get
    statistics about neighbor relationships in a lexicon, whereas
    get_neighbor_dict() is preferable when you want to know the neighbors for
    specific words.
    """
    sep = kwargs.get("sep", None)
    debug = kwargs.get("debug", None)
    corpus = kwargs.get("corpus", words)
    neighbors = []
    while words:
        word = words.pop()
        print(word) if debug else None
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
                neighbors.append((word, q) if __check_deletion(wsplit, qsplit) else None
            else:
                continue
    return neighbors



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
