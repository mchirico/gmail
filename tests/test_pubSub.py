# -*- coding: utf-8 -*-
from gmail.mail.mail import Mail
from .context import gmail
from gmail.pubsub.pubsub import PubSub
from gmail.bigQuery.bigquery import BigQ

from unittest import TestCase


class TestSuitePubSub(TestCase):
    """
    Yes, going across projects..
    # projects/septapig (NO) /topics/gmail-topic
    # quickstart-1586788855488 <---- Yes
    Advanced test cases."""

    def test_PubSub(self):
        p = PubSub()
        #p.send()
        p.read(2)

    def test_readMsgProcess(self):
        p = PubSub()
        p.send()
        p.readMsgProcess(5)


