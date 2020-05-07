# -*- coding: utf-8 -*-

from gmail.rejects.rejects import Rejects
from gmail.rejects.listing import rejects

from unittest import TestCase


class RejectsTestSuite(TestCase):
    """Advanced test cases."""

    def test_Rejects(self):
        r = Rejects()
        test = 'Return-Path: <Akshit@ustechsolutionsinc.com>'
        self.assertTrue(r.returnpath(test))

    def test_match(self):
        r = Rejects()
        self.assertFalse(r.returnpath('bob@gmail.com'))
        self.assertTrue(r.returnpath('bob@compugain.com'))

    def test_listing(self):
        r = rejects
        self.assertTrue('@pyramidci.com') in r
