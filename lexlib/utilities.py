#!/usr/bin/env python3

"""
Set of utilities for research involving words.
"""

# module: utilities
# copyright: 2016-2018 R. Steiner
# license: MIT License

import warnings


def deprecation_decorator(func):
    def wrapper(*args, **kwargs):
        msg = "Please use '{}' instead".format(func.__name__)
        warnings.warn(msg, DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper
