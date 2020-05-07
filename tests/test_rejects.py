# -*- coding: utf-8 -*-

from gmail.rejects.rejects import Rejects

from unittest import TestCase


class RejectsTestSuite(TestCase):
    """Advanced test cases."""

    def test_Rejects(self):
        r = Rejects()
        test = 'Return-Path: <Akshit@ustechsolutionsinc.com>'
        self.assertTrue(r.returnpath(test))
