# -*- coding: utf-8 -*-
from time import sleep

from gmail.mail.mail import Mail
from .context import gmail
from gmail.bigQuery.bigquery import BigQ

from unittest import TestCase


class AdvancedTestSuite(TestCase):
    """Advanced test cases."""


    def test_BigQ(self):
        b = BigQ()
        print(b.getTime())
        #b.mdo('mike','b','s')
        # self.assertEqual("we stuff", j.stuff())

    def test_DeleteBounce(self):
        b = BigQ()
        print(b.deleteBounce())

    def test_DeleteMsg(self):
        m = Mail()
        service = m.getService()
        message = m.create_message('mc@cwxstat.com',
                                   'mc@cwxstat.com',
                                   'Test Msg -',
                                   'Test msg delete*')
        m.populateSnippet()
        sleep(1)
        b = BigQ()
        result = b.deleteMsg('%Test msg delete%')
        self.assertEqual(result.state,'DONE')

