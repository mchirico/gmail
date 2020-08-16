# -*- coding: utf-8 -*-
from .context import gmail
from gmail.utils.mainprogram import MainProcess

from unittest import TestCase


# TODO:
#  This runs everything... the main process
#  Work backwards from here and refactoring
class MainUtilsTestSuite(TestCase):
    """This should run everything"""

    def test_Utils(self):
        MainProcess()
