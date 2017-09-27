# CHANGELOG

## 2.0

* Adds `get_neighbor_types()`, which determines the type of neighbor relationship (deletion, addition, or substitution) for sets of neighbors.
* Splits `get_neighbors()` into two functions (**`get_neighbors()` is now deprecated and should be removed in the next minor release**):
  * `get_neighbor_dict()`, which is essentially the original, useful for when you want a list of all the neighbors for particular words,
  * `get_neighbor_pairs()`, which returns a list of `(word, neighbor)` pairs, useful for when you want a list of all the unique neighbor pairs in a lexicon
    without specific interest in any individual words.
* No longer uses `pandas`, instead uses `csv`, which is in the standard library. **This changes the arguments of `get_words()` slightly:** `sep` is now
  `delimiter`, and the default value is now "," (was "`\t`"). Also allows for the use of any `csv.DictReader` formatting parameters.
* `filter_words()` is not `filter_by_nsyll()`, for improved clarity. **`filter_words()` is deprecated and should be removed in the next minor release.**
