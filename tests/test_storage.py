# -*- coding: utf-8 -*-
from datetime import datetime
from time import sleep

from gmail.analysis.analyze import Analyze
from gmail.mail.extract_eml import cleanBinaryEmail
from gmail.mail.mail import Mail
from gmail.storage.storage import Buckets

from .context import gmail
from gmail.bigQuery.bigquery import BigQ
from gmail.parsePandas.parse import Parse

from unittest import TestCase


class StorageTestSuite(TestCase):
    """test cases."""

    def test_Status(self):
        b = Buckets()
        msg = """
        Last run: {}
        """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%s"))
        b.createFromString("status/test_status.txt", msg)
