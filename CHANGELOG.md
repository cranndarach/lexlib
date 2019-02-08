# CHANGELOG

## 3.0
* Combines `syllables` and `consonant_clusters` into `structure`.
  * It's still possible to access all functions through the package's global namespace.
* Adds `structure.get_cv()` which finds the consonant-vowel structure of a word.
* Removes `get_neighbors()` and `filter_words()`, which were deprecated in 2.0.

## 2.2

* Adds `check_neighbors()`, which checks whether two words are neighbors. Reduces redundant code in neighbor-getting functions, and allows for boolean
  comparison of two words.
* Adds `clusters_word()`, which gets the consonant clusters for a single word, in contrast with `clusters()`, which gets the consonant clusters of a list of
  words.
* Fixes bug where lists provided as arguments were emptied. Now uses `list.copy()`.

## 2.1

* Adds `get_neighbor_positions()`, which determines the position at which a substitution neighbor relationship is formed.

## 2.0

* Adds `get_neighbor_types()`, which determines the type of neighbor relationship (deletion, addition, or substitution) for sets of neighbors.
* Splits `get_neighbors()` into two functions (**`get_neighbors()` is now deprecated and should be removed in the next minor release**):
  * `get_neighbor_dict()`, which is essentially the original, useful for when you want a list of all the neighbors for particular words,
  * `get_neighbor_pairs()`, which returns a list of `(word, neighbor)` pairs, useful for when you want a list of all the unique neighbor pairs in a lexicon
    without specific interest in any individual words.
* No longer uses `pandas`; instead uses `csv`, which is in the standard library. **This changes the arguments of `get_words()` slightly:** `sep` is now
  `delimiter`, and the default value is now "," (was "`\t`"). Also allows for the use of any `csv.DictReader` formatting parameters.
* `filter_words()` is now `filter_by_nsyll()`, for improved clarity. **`filter_words()` is deprecated and should be removed in the next minor release.**
