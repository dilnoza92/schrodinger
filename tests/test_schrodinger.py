#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_schrodinger
----------------------------------

Tests for `schrodinger` module.
"""

import argparse
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
        

        parser1=argparse.ArgumentParser()                  #parses command line inputs                  \
            
        parser1.add_argument('--fourier', nargs="?")       #adds a flag for fourier has to be a boolean \
            
        parser1.add_argument('--legendre', nargs="?")      #adds a flag for legendre has to be a boolean
        parser1.add_argument('--constant', nargs="?")          #adds a flag for constant                 
        parser1.add_argument('--potential_energy', nargs="?")  #adds a flag for potential energy         
        parser1.add_argument('--input_file', nargs="?")        #adds a flag for input file               
        parser1.add_argument('--basis_set_size', nargs="?")    #adds a flag for basis set size           
        parser1.add_argument('schrodinger/schrodinger.py', nargs='?')#makes sure that parser doesn't giv\
            
        arguments=parser1.parse_args()     
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
