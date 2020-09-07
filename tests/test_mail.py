# -*- coding: utf-8 -*-
import pytest

from gmail.analysis.analyze import Analyze
from .context import gmail
from gmail.mail.mail import Mail
from gmail.bigQuery.bigquery import BigQ
from unittest.mock import patch
import pickle

from unittest import TestCase


class MailTestSuite(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        m = Mail()
        service = m.getService()
        message = m.create_message('mc@cwxstat.com',
                                   'mc@cwxstat.com',
                                   'Test Msg -',
                                   'Test msg delete*')
        m.send_message(service, 'me', message)

    @classmethod
    def tearDownClass(cls) -> None:
        q = BigQ()
        q.deleteMsg('%Test msg delete%')

    """ Our end-to-end test """

    # def test_MessageGotIn(self):
    #     b = BigQ()
    #     result = b.select("""
    #     select count(*) as c from `septapig.mail.mc`
    #     where msg like 'Test msg delete%'
    #     """)
    #     for row in result:
    #         self.assertGreater(row['c'], 0)

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
                                   'Hope you are doing well!')
        id = m.send_message(service, 'me', message)
        self.assertGreater(len(id['id']), 10, 'No id returned')

    @pytest.mark.skip(reason="Sends out real message")
    def test_Reply(self):
        m = Mail()
        service = m.getService()
        message = m.create_static_reply(
            'Hope you are doing well!')
        id = m.send_message(service, 'me', message)
        self.assertGreater(len(id['id']), 10, 'No id returned')

    # TODO:
    #   Finish...
    #     https://github.com/mchirico/gmail/pull/71
    @patch('gmail.mail.mail.Mail.messageDelete')
    @patch('gmail.mail.mail.Mail.messageGet')
    @patch('gmail.mail.mail.Mail.messageList')
    def test_zMainP(self, messageList,
                   messageGet,
                   messageDelete):
        with open("fixtures/response.pkl", "rb") as pickle_in:
            messageList.return_value = pickle.load(pickle_in)
        with open("fixtures/message.pkl", "rb") as pickle_in:
            messageGet.return_value = pickle.load(pickle_in)
        messageDelete.return_value = 'done'
        m = Mail()
        m.populateSnippet()
        expected = 'Yes! Sample email for testing: Special Characters: ' \
                   '&#39;&quot; &quot;&quot;&quot; \\&quot; \\` ;'
        self.assertEqual(m.data[3][1], 'Return-Path: <mchirico@gmail.com>')
        self.assertEqual(m.data[3][2], expected)

    def test_Mail(self):
        m = Mail()
        q = BigQ()
        m.populateSnippet()
        for i in m.data:
            q.insert(i[0], i[1], i[2], i[4], i[5])

        # self.assertEqual("we stuff", j.stuff())

    def test_Delete_msg(self):
        q = BigQ()
        q.deleteMsg('%Hope you are doing well%')
        q.deleteMsg('%Test msg delete*%')

    def test_GetService(self):
        m = Mail()
        service = m.getService()
        # m.watch(service)

    def test_GetServiceDeadMail(self):
        m = Mail('dead')
        service = m.getServiceDeadMail()
        m.populateSnippetDeadMail()

    def test_buildDeadLabels(self):
        m = Mail('dead')
        service = m.getServiceDeadMail()
        r = m.buildDeadLabels('TEST')
        self.assertIn('TRASH', r)

    # FIXME: 
    #      Need to update code
    def test_Analytics(self):
        a = Analyze()
        a.runAnalyze()
