#!/usr/bin/env python3


def get_neighbor_types(neighbor_dict):
    """
    Takes a dict of neighbors (where a key is a "target" word and its value is a
    list of all of its neighbors) and returns a list of (word1, word2,
    relationship) triples, where `relationship` is one of "deletion,"
    "addition," "substitution," or "unknown".

    arguments:
        neighbor_dict -- a dict whose keys are target words, and their values are
        a list of their neighbors (e.g., the output of get_neighbor_dict()).
    """
    types = []
    targets = neighbor_dict.keys()
    while targets:
        current = targets.pop()
        for neighbor in neighbors:
            if len(current) == len(neighbor): # if they are the same length, the change was a substitution
                types.append((current, neighbor, "substitution"))
            elif len(current) > len(neighbor): # if the target is longer than the neighbor, the change was a deletion
                types.append((current, neighbor, "deletion"))
            elif len(current) < len(neighbor): # if the target is shorter than the neighbor, the change was an addition
                types.append((current, neighbor, "addition"))
            else: # just to be sure
                types.append((current, neighbor, "unknown"))
    return types
