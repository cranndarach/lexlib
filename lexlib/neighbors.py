#!/usr/bin/env python3

"""
Neighbor calculation functions for lexlib.
"""

# module: neighbors
# copyright: 2016-2018 R. Steiner
# license: MIT License


def get_neighbor_dict(words, **kwargs):
    """
    Compare each word in a list of *words* to each word in a *corpus*
    word list (or in the same list if *corpus* is not given), and return
    a dict where each target word is a key, and its value is a list of
    its neighbors. (If you are looking for a function to get neighbor
    pairs, see `get_neighbor_pairs()`).

    keyword arguments:
        *corpus* -- List of all the words to get the neighbors from. If
        empty, defaults to *words*.

        *sep* -- String used to separate phonemes (if the words are
        phonological forms). To separate into individual characters,
        set to `None` (default).

        *debug* -- If `True`, it prints the current word and the words
        being compared to it to the console. Defaults to `False`.
    """
    words = words.copy()
    sep = kwargs.get("sep", None)
    debug = kwargs.get("debug", None)
    corpus = kwargs.get("corpus", words).copy()
    neighbors = {}
    while words:
        word = words.pop()
        print(word) if debug else None
        w_split = list(word) if not sep else word.split(sep)
        nbrs = filter(lambda tgt: check_neighbors(w_split, tgt, sep), corpus)
        neighbors[word] = list(nbrs)
    return neighbors


def check_neighbors(a, b, sep=None):
    """
    Determine whether two words are neighbors. Returns `True` if they
    are neighbors and `False` if they are not.

    *sep* -- String used to separate phonemes (if the words are
    phonological forms). To separate into individual characters, set to
    `None` (default).
    """
    if type(a) == list:
        a_split = a
        b_split = list(b) if not sep else b.split(sep)
    elif sep:
        a_split = a.split(sep)
        b_split = b.split(sep)
    else:
        a_split = list(a)
        b_split = list(b)
    a_len = len(a_split)
    b_len = len(b_split)
    if b_len == a_len:
        if __check_substitution(a_split, b_split):
            return True
    elif b_len == a_len+1:
        if __check_addition(a_split, b_split):
            return True
    elif b_len == a_len-1:
        if __check_deletion(a_split, b_split):
            return True
    else:
        return False


def get_neighbor_pairs(words, **kwargs):
    """
    Compare each word in a list of *words* to each word in a *corpus*
    word list (or in the same list if *corpus* is not given), and return
    a list of `(word, neighbor)` pairs. (If you are looking for a
    function to get lists of all the neighbors for specific words, see
    `get_neighbor_pairs()`).

    keyword arguments:
        *corpus* -- List of all the words to get the neighbors from. If
        omitted, defaults to `words`.

        *sep* -- String used to separate phonemes (if the words are
        phonological forms). To separate into individual characters, set
        to `None` (default).

        *debug* -- If True, it logs the current word and the words being
        compared to it to the console. Defaults to False.
    """
    words = words.copy()
    sep = kwargs.get("sep", None)
    debug = kwargs.get("debug", None)
    corpus = kwargs.get("corpus", words).copy()
    neighbors = []
    while words:
        word = words.pop()
        print(word) if debug else None
        # Lighten the memory load and avoid duplicates.
        if word in corpus:
            corpus.remove(word)
        w_split = list(word) if not sep else word.split(sep)
        nbrs = filter(lambda tgt: check_neighbors(w_split, tgt, sep), corpus)
        neighbors += [(word, nbr) for nbr in nbrs]
    return neighbors


def get_neighbor_positions(neighbor_pairs, sep=None):
    """
    Given a list of `(word1, word2)` *neighbor_pairs*, return a list of
    `(word1, word2, position)` triples, where `position` is the position
    in the words where the neighbor relationship is formed. Note that
    this can only be calculated for pairs of substitution neighbors. If
    the words differ in length, `position` will be `-1`.

    Example::

        >>> neighbor_pairs = [("cat", "cap"), ("cat", "cut"), ("cat", "cast")]
        >>> get_neighbor_positions(neighbor_pairs)
        [("cat", "cap", 3), ("cat", "cut", 2), ("cat", "cast", -1)]

    """
    return [__get_position(neighbors, sep=None) for neighbors in
            neighbor_pairs]


def get_neighbor_types(neighbor_dict, sep=None):
    """
    Given a *neighbor_dict* (where a key is a "target" word and its
    value is a list of all of its neighbors), return a list of `(word1,
    word2, relationship)` triples, where `relationship` is one of
    "deletion," "addition," "substitution," or "unknown".
    """
    types = []
    targets = list(neighbor_dict.keys())
    while targets:
        current = targets.pop()
        # In case it gets split, use this as the key.
        current_key = current
        if sep:
            current = current.split(sep)
        for neighbor in neighbor_dict[current_key]:
            # Misnomer, just to add to list.
            neighbor_key = neighbor
            if sep:
                neighbor = neighbor.split(sep)
            # If they are the same length, the change was a substitution.
            if len(current) == len(neighbor):
                types.append((current_key, neighbor_key, "substitution"))
            # If the target is longer than the neighbor, the change was
            # a deletion.
            elif len(current) > len(neighbor):
                types.append((current_key, neighbor_key, "deletion"))
            # If the target is shorter than the neighbor, the change
            # was an addition.
            elif len(current) < len(neighbor):
                types.append((current_key, neighbor_key, "addition"))
            else:
                types.append((current_key, neighbor_key, "unknown"))
    return types


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


def __get_position(neighbors, sep=None):
    first, second = neighbors
    if sep:
        first = first.split(sep)
        second = second.split(sep)
    if len(first) != len(second):
        return (first, second, -1)
    for pos in range(len(first)):
        if first[pos] != second[pos]:
            return (first, second, pos+1)
    else:
        return (first, second, 0)
