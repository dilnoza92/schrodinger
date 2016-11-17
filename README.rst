===============================
schrodinger
===============================


.. image:: https://img.shields.io/pypi/v/schrodinger.svg
        :target: https://pypi.python.org/pypi/schrodinger

.. image:: https://img.shields.io/travis/dilnoza92/schrodinger.svg
        :target: https://travis-ci.org/dilnoza92/schrodinger

.. image:: https://readthedocs.org/projects/schrodinger/badge/?version=latest
        :target: https://schrodinger.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/dilnoza92/schrodinger/shield.svg
     :target: https://pyup.io/repos/github/dilnoza92/schrodinger/
     :alt: Updates

.. image:: https://coveralls.io/repos/github/dilnoza92/schrodinger/badge.svg?branch=master
:target: https://coveralls.io/github/dilnoza92/schrodinger?branch=master




solution to the schrodinger's equation


* Free software: GNU General Public License v3
* Documentation: https://schrodinger.readthedocs.io.


How to run the code with inputs given in the terminal
--------

* in the terminal type for example the following can be typed:

* coverage run --source=schrodinger/schrodinger.py  schrodinger/schrodinger.py  --fourier True --legendre False --constant 1 --basis_set_size 20 --potential_energy 1 --input_file Pot_example1.txt


* In order to read the input, Pot_example1.txt file should be in the main directory which will contain the potential energy for different positions.

* The domain over which the wavefunction is defined is [-1,1] and the variable is called 'positions'

* The basis_set_size is the size of the basis set

* The constant is a 'constant' variable

* The wavefunction I chose is (sin(2*pi*t)+t**3)

* legendre is a boolean that is true if legendre polynomials should be used and fourier should be set false

* fourier is a boolean that is true if fourier series should be used and legendre should be set false

* The output will be a vector of coefficient for a partical choice of basis set and will be displayed on the terminal 
 
* The comparison of fourier, legendre and the original wavefunction is given below:

.. image:: https://github.com/dilnoza92/schrodinger/blob/master/schrodinger/fourier1.png   

How to run the tests
-------

* To run the test type the following:

* coverage run setup.py test

* coverage report -m

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

