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

from schrodinger import schrodinger
#from schrodinger import cli



class TestSchrodinger(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_answer(self):
        self.assertEqual(schrodinger.answers[1],1)

