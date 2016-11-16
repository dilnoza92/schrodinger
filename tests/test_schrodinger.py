#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_schrodinger
----------------------------------

Tests for `schrodinger` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner
import numpy as np
from schrodinger import schrodinger
#from schrodinger import cli



class TestSchrodinger(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass


    def test_final_deriv(self):
       # schrodinger.legendre_check==False
        #schrodinger.fourier_check=True
        #answers=[]
        #answers=schrodinger.final_fourier_deriv()
        #print answers
        #print schrodinger.laplacian(True,schrodinger.legendre_coeff)
        #self.assertEqual(len(schrodinger.hamiltonian_fourier(schrodinger.legendre_coeff)),len(answers))
        schrodinger.legendre_check==True
        schrodinger.fourier_check=False
        print schrodinger.legendre_coeff
        answers1=[]
        answers1=np.polynomial.legendre.legder(schrodinger.legendre_coeff,2)
        #print schrodinger.laplacian(True,schrodinger.legendre_coeff)
        
        self.assertEqual(len(schrodinger.laplacian(True, schrodinger.legendre_coeff)),len(answers1))
        pass




    def test_answer(self):
        self.assertEqual(schrodinger.answers[1],1)
        results=schrodinger.answer(True)
        self.assertEqual(results[1],1)
        pass

    def test_potential_force_data(self):
        self.assertRaises(ValueError,schrodinger.potential_force_data,None)
        pass
