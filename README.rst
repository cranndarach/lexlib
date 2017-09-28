========
 lexlib
========

    Python package containing functions that may be useful for word research.

.. image:: https://badge.fury.io/py/lexlib.svg
    :target: https://badge.fury.io/py/lexlib

.. image:: https://anaconda.org/cranndarach/lexlib/badges/version.svg
    :target: https://anaconda.org/cranndarach/lexlib

.. note:: This project is a work in progress. New functions may be added at
   any point. See `CHANGELOG.md`_ for important changes.

.. _CHANGELOG.md: https://github.com/cranndarach/lexlib/blob/master/CHANGELOG.md

--------
 Topics
--------

* **clusters:** Extract consonant clusters from a list of words.
* **neighbors:** Find the phonological neighbors for words using the
  one-phoneme deletion, addition, or substitution rule (Luce & Pisoni, 1998),
  or find what relationship makes pairs of words neighbors.
* **syllables:** Get the syllable count for individual words or a list of
  words, or filter lists of words by number of syllables.

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

git clone
'''''''''

::

    git clone https://github.com/cranndarach/lexlib.git
    cd lexlib
    # using pip
    pip install
    # or using setuptools
    python setup.py install

tarball
'''''''

`Download the latest release <https://github.com/cranndarach/lexlib/releases>`_

In a terminal (remember to update the path):

::

    cd path/to/downloaded/lexlib-{M.m.P}.tar.gz
    tar -xzvf lexlib-{M.m.P}.tar.gz
    cd lexlib-{M.m.P}/
    # using pip
    pip install
    # or using setuptools
    python setup.py install

-------
 Usage
-------

To import the package to use in your project
""""""""""""""""""""""""""""""""""""""""""""

::

    import lexlib as lx

For documentation on specific functions, see the `docs/` directory or the
`HTML version`_ or enter `help(lx.function_name)` into your interpreter.

.. _HTML version: http://lexlib.readthedocs.io

---------
 License
---------

This package is licensed under the terms of the MIT license, copyright (c)
2016-2017 R. Steiner.

------------
 References
------------

Luce, P. A., & Pisoni, D. B. (1998). Recognizing spoken words: The neighborhood
activation model. *Ear and Hearing, 19*\ (1), 1.
