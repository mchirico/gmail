# -*- coding: utf-8 -*-

from .context import gmail
from gmail.bigQuery.bigquery import BigQ

from unittest import TestCase


class AdvancedTestSuite(TestCase):
    """Advanced test cases."""


    def test_BigQ(self):
        b = BigQ()
        #b.mdo('mike','b','s')
        # self.assertEqual("we stuff", j.stuff())
