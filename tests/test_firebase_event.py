# -*- coding: utf-8 -*-
from time import sleep

import pytest

from gmail.mail.mail import Mail
from .context import gmail
from gmail.bigQuery.bigquery import BigQ
from gmail.parsePandas.parse import Parse
from firebase.firebase import FBmail

from unittest import TestCase
import threading
import time


class FirebaseEventTestSuite(TestCase):
    """Advanced test cases."""

    @pytest.mark.skip(reason="WIP")
    def test_event(self):

        f = open('/Users/rommel/gmail/src/github.com/mchirico/gmail/log', 'w')
        fbmail = FBmail()
        event = threading.Event()


        def mylog(msg):
            f.write('  {}\n'.format(str(msg)))
            f.flush()

        s = fbmail.event(event,mylog)

        def start_operations():
            for i in range(0, 23):
                f.write('start: {}\n'.format(i))
                f.flush()
                event.wait()
                if event.is_set():
                    f.write('set: {}\n'.format(i))
                    f.flush()
                    event.clear()


        t1 = threading.Thread(target=start_operations)
        #t0.start()
        t1.start()
        time.sleep(29)
        s.unsubscribe()
        mylog("unsubscribed")
        time.sleep(300)
