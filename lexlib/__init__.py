#!/usr/bin/env python3

"""
Set of utilities for research involving words.
"""

# copyright: 2016-2018 R. Steiner
# license: MIT License

from .consonant_clusters import *
from .io import *
from .neighbors import *
from .syllables import *
from .utilities import *

__all__ = ["check_neighbors", "get_words", "clusters", "clusters_word",
           "get_neighbor_dict", "get_neighbor_pairs", "get_neighbor_positions",
           "get_neighbor_types", "get_neighbors", "nsyll_list", "nsyll_word",
           "filter_by_nsyll", "filter_words"]

get_neighbors = deprecation_decorator(get_neighbor_dict)
filter_words = deprecation_decorator(filter_by_nsyll)
