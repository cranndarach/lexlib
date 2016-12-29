#!/usr/bin/env python3

"""
module: get_neighbor.py
author: R Steiner
license: MIT License, copyright (c) 2016 R Steiner
description: Functions to find the phonological neighbors of a list of words.
"""

import json


def neighbors(words, corpus, sep=None, debug=False):
    """
    Iterates through the word list, comparing each word in the
    corpus to the current word in length, and passing it to the
    appropriate "checker" function, or moving on if its length
    indicates that it is not a neighbor. If the checker returns
    True, then it appends that word to the current word's "neighbor"
    entry.

    keyword arguments:
        words -- Path to the file containing the words whose
        neighbors will be found. Should contain forms only, one per line.
        corpus -- Path to the file containing the corpus. Forms only,
        one per line.
        sep -- String used to separate phonemes in the phonological forms.
        To separate into individual characters, set to None (default).
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
