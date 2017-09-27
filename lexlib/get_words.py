#!/usr/bin/env python3

"""
module: get_words.py
author: R. Steiner
license: MIT license, copyright (c) 2016, 2017 R. Steiner
description: Function for retrieving only the specified column from a
spreadsheet-shaped corpus.
"""

import csv


def get_words(file_path, column_name, delimiter=",", **fmtparams):
    """
    Returns a list containing only the specified column.

    arguments:
    file_path -- path to the file containing the corpus (a CSV or tab-separated
    text file, etc.).
    column_name -- the name of the column in the given file that contains the words.
    delimiter -- the string separating the cells in the database. Default: ","
    **fmtparams -- any additional formatting arguments for the built-in
    `csv.reader` function.
    """
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter, **fmtparams)
        words = [row[column_name] for row in reader]
    return words
