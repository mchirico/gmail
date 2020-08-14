# -*- coding: utf-8 -*-
from datetime import datetime
from time import sleep

from gmail.analysis.analyze import Analyze
from gmail.mail.extract_eml import cleanBinaryEmail
from gmail.mail.mail import Mail
from gmail.storage.storage import Buckets
from gmail.utils.mainprogram import MainProcess

from .context import gmail
from gmail.bigQuery.bigquery import BigQ
from gmail.parsePandas.parse import Parse

from unittest import TestCase


# TODO:
#  This runs everything... the main process
#  Work backwards from here and refactoring
class MainUtilsTestSuite(TestCase):
    """This should run everything"""

    def test_Utils(self):
        MainProcess()
