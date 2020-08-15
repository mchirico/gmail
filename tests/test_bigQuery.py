# -*- coding: utf-8 -*-
from time import sleep

from gmail.mail.extract_eml import cleanBinaryEmail
from gmail.mail.mail import Mail

from .context import gmail
from gmail.bigQuery.bigquery import BigQ
from gmail.parsePandas.parse import Parse

from unittest import TestCase


class BigQueryTestSuite(TestCase):
    """Advanced test cases."""

    def test_filter(self):
        b = BigQ()

    def test_DeleteBounce(self):
        b = BigQ()
        print(b.deleteBounce())

    # TODO: Refactor
    def test_d(self):
        b = BigQ()
        # b.select('drop table IF EXISTS `septapig.mail.tmp0`')

        d = b.d()
        p = Parse(d)
        p.raw().subject().date().received().save()
        query = """
        insert into  `septapig.mail.parsed` 
SELECT b.* FROM `septapig.mail.parsed` a
right outer join `septapig.mail.tmp0` b
on a.id = b.id
where a.id is null
        """
        result = b.select(query)
        [x for x in result]

        print(p.d)

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
        result = b.deleteMsgDays('%Test msg delete%', -2)
        self.assertEqual(result.state, 'DONE')
