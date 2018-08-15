========
 lexlib
========

    Python library for some utilities that may be useful for word research.

.. image:: https://badge.fury.io/py/lexlib.svg
    :target: https://badge.fury.io/py/lexlib

.. image:: https://anaconda.org/cranndarach/lexlib/badges/version.svg
    :target: https://anaconda.org/cranndarach/lexlib

.. note:: This project is a work in progress. New functions may be added at
   any point. See `CHANGELOG.md`_ for important changes.

.. _CHANGELOG.md: https://github.com/cranndarach/lexlib/blob/master/CHANGELOG.md

----------
 Features
----------

* Extract consonant clusters from a word or list of words.
* Find neighbors of words.
* Other neighbor utilities, e.g., type of neighbor relationship, position of
  divergence.
* Get the syllable count for words or a list of words, or filter lists of words
  by number of syllables.

--------------
 Requirements
--------------

* Python 3

--------------
 Installation
--------------

Using pip install
"""""""""""""""""

::

    pip3 install lexlib

Using conda install
"""""""""""""""""""

::

    conda install -c cranndarach lexlib

From source
"""""""""""

`git clone` for the development version
'''''''''''''''''''''''''''''''''''''''

::

    git clone https://github.com/cranndarach/lexlib.git
    cd lexlib
    pip install

Download a release
''''''''''''''''''

`Download the latest release <https://github.com/cranndarach/lexlib/releases>`_

In a terminal (remember to update the path):

::

    cd path/to/download/lexlib-x.y.z.tar.gz
    tar -xvf lexlib-x.y.z.tar.gz
    cd lexlib-x.y.z/
    pip install

-------
 Usage
-------

To import the package to use in your project
""""""""""""""""""""""""""""""""""""""""""""

::

    import lexlib as lx

.. note::

  All of the submodules are imported by lexlib. That means that you can call,
  for example, `lx.get_neighbor_pairs()` instead of `lx.neighbors.get_neighbor_pairs()`.

For documentation on specific functions, see the `docs/` directory or the
`online documentation`_ or enter `help(lx.function_name)` into your interpreter.

.. _online documentation: http://lexlib.readthedocs.io

---------
 License
---------

This package is licensed under the terms of the MIT license, copyright (c)
2016-2018 R. Steiner.
