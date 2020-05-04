# -*- coding: utf-8 -*-
from time import sleep

from gmail.mail.mail import Mail
from .context import gmail
from gmail.bigQuery.bigquery import BigQ
from gmail.parsePandas.parse import Parse
from firebase.firebase import FBmail

from unittest import TestCase


class FirebaseTestSuite(TestCase):
    """Advanced test cases."""

    def test_BigQ(self):
        b = BigQ()
        print(b.getTime())
        # b.mdo('mike','b','s')
        # self.assertEqual("we stuff", j.stuff())

    def test_Delete(self):
        fbmail = FBmail()
        for i in range(0, 5):
            fbmail.delete(i)

    def test_FBMail(self):
        b = BigQ()
        query = """
        
        SELECT msg,EXTRACT(DATE FROM timestamp) AS date,a.d FROM 
        `septapig.mail.parsed`, 
 (SELECT DATE_ADD(CURRENT_DATE(), INTERVAL -2 DAY) as d) a
where subject like 'R% C%'
 and date >= cast(a.d as STRING)
 order by date desc
 
                """
        result = b.select(query)
        fbmail = FBmail()
        count = 0
        for row in result:
            fbmail.update(count, row['msg'], row['date'])
            print(row['date'])
            count += 1

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
