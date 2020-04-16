# -*- coding: utf-8 -*-

from .context import gmail
from gmail.mail.mail import Mail
from gmail.bigQuery.bigquery import BigQ

from unittest import TestCase


class AdvancedTestSuite(TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(gmail.hmm())

    def test_pickle(self):
        m = Mail()
        a = '234'
        m.pickle_it("fixtures/obj.pkl", a)
        r = m.unpickle_it("fixtures/obj.pkl")
        self.assertEqual(a, r)

    def test_response(self):
        m = Mail()
        r = m.unpickle_it("fixtures/message.pkl")
        print(r)
        self.assertEqual(r['id'], '1717a15dc100f5bd')

    def test_CreateEmail(self):
        m = Mail()
        service = m.getService()
        message = m.create_message('mc@cwxstat.com',
                                   'mc@cwxstat.com',
                                   'Test Msg -',
                                   'Test msg delete*')
        id = m.send_message(service, 'me', message)
        self.assertGreater(len(id['id']), 10, 'No id returned')

    def test_Mail(self):
        m = Mail()
        q = BigQ()
        m.main()
        for i in m.data:
            q.insert(i[0], i[1], i[2], i[4])

        # self.assertEqual("we stuff", j.stuff())

    def test_Delete_msg(self):
        q = BigQ()
        q.deleteMsg('%Test msg delete%')

    def test_GetService(self):
        m = Mail()
        service = m.getService()
