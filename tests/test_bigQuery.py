# -*- coding: utf-8 -*-
from time import sleep

from gmail.mail.mail import Mail
from .context import gmail
from gmail.bigQuery.bigquery import BigQ
from gmail.parsePandas.parse import Parse

from unittest import TestCase


class AdvancedTestSuite(TestCase):
    """Advanced test cases."""

    def test_CreateEML(self):
        b = BigQ()

    # FIXME: Clean up... this actually write out email
    def test_BigQ(self):
        b = BigQ()
        row = b.createEML()
        data = [c['txt'] for c in row][0]
        email = data[2:-1].replace('\\r\\n', '\n')
        f = open('junk.eml', 'w')
        f.write(email)
        f.close()
        self.assertEqual(email[0:20], 'Delivered-To: mc@cwx')

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
        result = b.deleteMsg('%Test msg delete%')
        self.assertEqual(result.state, 'DONE')
