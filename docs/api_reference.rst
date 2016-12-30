##########################
 lexlib API Documentation
##########################

``lexlib.clusters(words, vowels[, sep=None])``
==============================================

Extract consonant clusters from a list of words.

**Returns** a non-unique *list* of consonant clusters from the given list of
words.

Arguments:
----------

* **words:** *List* of the word forms to extract clusters from.
* **vowels:** *List* of vowels.
* **sep:** *String* that separates phonemes/letters/segments. default: ``None``
  (separate into individual characters).

``lexlib.get_words(file_path, column[, sep="\t"])``
===================================================

Retrieve only the column of interest from a data frame-like corpus. Specifically
intended for extracting words, but has flexibility.

**Returns** a *list* containing the values in the column specified (typically,
this will be a list of individual word forms).

Arguments:
----------

* **file_path:** Path to the file (a *string*) containing the corpus. The file
  should be a delimited text file (spreadsheet-style), such as a ``.csv`` or
  tab-separated ``.txt`` file.
* **column:** Name of the column (a *string*) containing the words in the
  database file.
* **sep:** String separating the cells. Defaults to "\t" (tab). For a ``.csv``
  file, use ","

``lexlib.neighbors(words, corpus[, sep=None, debug=False])``
============================================================

Find the phonological neighbors of a list of words using the one-phoneme
deletion, addition, or substitution rule (Luce & Pisoni, 1998).

**Returns** a *dict* with query words as keys and a *list* of their neighbors
as the values.

Arguments:
----------

* **words:** Path to the file (a *string*) containing the query words. Should
  contain forms only, one per line.
* **corpus:** Path to the file (a *string*) containing the corpus. Forms only,
  one per line.
* **sep:** *String* to use as the delimiter for dividing the words in the
  corpus into phonemes. To separate into individual characters, set to ``None``.
  default: "."
* **debug:** If ``True``, prints the current word and the words being compared
  to it to the console. Defaults to ``False``, but if you tend to worry, you
  will likely want to set it to ``True``.

``lexlib.syllable_filter(corpus, vowels, nsyll[, sep=None])``
=============================================================

Extract words with the desired number of syllables from a list, heuristically,
using vowels as indicators of syllables.

**Returns** a *list* of the words meeting the given syllable criteria.

Arguments:
----------

* **corpus:** *List* of words (only the word forms) to filter.
* **vowels:** *List* of the vowels used in the corpus.
* **nsyll:** An *integer* **or *list of integers*** reflecting the number of
  syllables desired. Using a list of integers will return words of any of
  those lengths.
* **sep:** *String* to use as the delimiter for dividing the words in the
  corpus into phonemes. default: ``None`` (separates into individual characters)
