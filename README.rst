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

.. image:: https://coveralls.io/repos/github/dilnoza92/schrodinger/badge.png?branch=master
:target: https://coveralls.io/github/dilnoza92/schrodinger?branch=master




solution to the schrodinger's equation


* Free software: GNU General Public License v3
* Documentation: https://schrodinger.readthedocs.io.


Features
--------

* TODO

*In order to read the input, Pot_example1.txt file should be in the main directory which will contain the potential energy for different positions.

*If one wants to use legendre basis set he or she should open the schodinger/schrodinger.py file and change the variables fourier_check=False and legendre_check=True
* The fourier is vice versa

*the constant should be set in 'constant' variable

*the wavefunction I chose is (sin(2*pi*t)+t**3)

* the domain over which the wavefunction is defined is [-1,1] and the variable is called 'positions'

* the size of the basis set is called 'size_basis_set'
 
* one can change the position value by changing the value of 'x1'

The example uses x1=0.5, size of the basis set is 150

The output will be displayed on the terminal 
 





Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

