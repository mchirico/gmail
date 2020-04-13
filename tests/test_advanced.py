# -*- coding: utf-8 -*-

from .context import gmail
from gmail.util.mail import Junk, Mail
from gmail.bigQuery.bigquery import BigQ

from unittest import TestCase


class AdvancedTestSuite(TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(gmail.hmm())

    def test_junk(self):
        j = Junk()
        self.assertEqual("we stuff", j.stuff())

    def test_Mail(self):
        m = Mail()
        q = BigQ()
        m.main()
        for i in m.data:
            q.insert(i[0],i[1],i[2])

        # self.assertEqual("we stuff", j.stuff())
