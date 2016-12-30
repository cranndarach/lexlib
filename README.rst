========
 lexlib
========

    Python package containing functions that may be useful for word research.

.. image:: https://badge.fury.io/py/lexlib.svg
    :target: https://badge.fury.io/py/lexlib
    
.. image:: https://anaconda.org/cranndarach/lexlib/badges/version.svg
    :target: https://anaconda.org/cranndarach/lexlib

.. note:: This project is a work in progress. New functions may be added at
   any point. I will use `semantic versioning <https://semver.org>`_ to make
   the impact of any changes to the package clear.

------------------
 Package Contents
------------------

* **clusters:** Extract consonant clusters from a list of words.
* **neighbors:** Find the phonological neighbors of a list of words using the
  one-phoneme deletion, addition, or substitution rule (Luce & Pisoni, 1998).
* **syllable_filter:** Extract words with the desired number of syllables
  from a list.
* **words_only:** Retrieve only the column of interest from a data frame-like
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

    cd path/to/downloaded/lexlib-M.m.P.tar.gz
    tar -xzvf lexlib-M.m.P.tar.gz
    cd lexlib-M.m.P/
    # using pip
    pip install
    # or using setuptools
    python setup.py install

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
