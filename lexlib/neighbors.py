#!/usr/bin/env python3

"""
module: get_neighbor.py
author: R Steiner
license: MIT License, copyright (c) 2016 R Steiner
description: Functions to find the phonological neighbors of a list of words.
"""


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
