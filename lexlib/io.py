#!/usr/bin/env python3

"""
Functions for reading and writing files.
"""

# module: io
# copyright: 2016-2018 R. Steiner
# license: MIT License

import csv


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
