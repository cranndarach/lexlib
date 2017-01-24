#!/usr/bin/env python3

"""module: syllables
author: R Steiner
license: MIT, copyright (c) 2016 R Steiner
description: Functions for working with syllables: currently counting
and filtering a corpus by number of syllables.
"""


def __decorator(fnc):
    return fnc


# Does this have a purpose anymore, or is it a relic from when this was a class?
# Might be time to deprecate...
def __load_file(filepath):
    with open(filepath, 'r') as f:
        corpus = [word[:-1] for word in f]
    return corpus

load_corpus = __decorator(__load_file)
load_vowels = __decorator(__load_file)


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
    Counts the number of syllables for a list of words. Returns a list
    of (word, nsyll) pairs.

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


def filter_words(corpus, vowels, nsyll, sep=None):
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
    match = list(filter(lambda w: nsyll_word(w, vowels, sep) in
                        nsyll, corpus))
    return match
