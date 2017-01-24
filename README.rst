========
 lexlib
========

    Python package containing functions that may be useful for word research.

.. note:: This project is a work in progress. New functions may be added at
   any point.

------------------
 Package Contents
------------------

* **clusters:** Extract consonant clusters from a list of words.
* **neighbors:** Find the phonological neighbors of a list of words using the
  one-phoneme deletion, addition, or substitution rule (Luce & Pisoni, 1998).
* **nsyll_word** and **nsyll_list:** Get the syllable count for individual
  words or a list of words.
* **syllable_filter:** Extract words with the desired number of syllables
  from a list.
* **get_words:** Retrieve only the column of interest from a data frame-like
  corpus. Specifically intended for extracting words, but has flexibility.

--------------
 Requirements
--------------

* Python 3 (developed with 3.5)
* pandas (developed with 0.18.1)

--------------
 Installation
--------------

Using pip install
"""""""""""""""""

::

    pip3 install lexlib

From source
"""""""""""

::

    git clone https://github.com/cranndarach/lexlib.git
    cd lexlib
    python setup.py install --user


-------
 Usage
-------

To import the package to use in your project
""""""""""""""""""""""""""""""""""""""""""""

::

    import lexlib as lx

For documentation on specific functions, see the `docs/` directory or the
`HTML version`_ or enter `help(lx.function_name)` into your interpreter.

.. _HTML version: http://pythonhosted.org/lexlib

---------
 License
---------

This package is licensed under the terms of the MIT license, copyright (c)
2016 R. J. Steiner.

------------
 References
------------

Luce, P. A., & Pisoni, D. B. (1998). Recognizing spoken words: The neighborhood
activation model. *Ear and Hearing, 19*\ (1), 1.
