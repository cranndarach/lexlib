#!/usr/bin/env python3

"""
module: words_only
author: R Steiner
license: MIT license, copyright (c) 2016 R Steiner
description: Function for retrieving only the specified column
from a corpus.
"""

import pandas as pd


def get_words(file_path, column, sep="\t"):
    """
    Returns a list containing only the specified column.
    get_words(file_path, column, sep="\t")

    Arguments:
    file_path -- path to the file containing the corpus (a CSV or tab-separated
    text file, etc.).
    column -- the name of the column in the given file that contains the words.
    sep -- the string separating the cells. Defaults to "\t" (tab).
    """
    frame = pd.read_csv(file_path, sep)
    word_series = frame[column]
    words = word_series.tolist()
    return words
