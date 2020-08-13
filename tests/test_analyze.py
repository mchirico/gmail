# -*- coding: utf-8 -*-
from time import sleep

from gmail.analysis.analyze import Analyze
from gmail.mail.extract_eml import cleanBinaryEmail
from gmail.mail.mail import Mail

from .context import gmail
from gmail.bigQuery.bigquery import BigQ
from gmail.parsePandas.parse import Parse

from unittest import TestCase


class AnalyzeTestSuite(TestCase):
    """test cases."""

    # def test_queryParsedEMLnoTXT(self):
    #     a = Analyze()
    #     r = a.queryParsedEMLnoTXT(3)
    #     print(r)

    def test_WriteLatest(self):
        a = Analyze()
        r = a.analyzeEML(1)
        if len(r[4]) > 0:
            a.emailAlert('mchirico@gmail.com', r[4][0])
        files = ['email/last.eml', 'email/last2.eml']
        a.writeEML(r[1], files)
        a.updateAnalysisTable(files[0])
