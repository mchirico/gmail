from google.cloud import bigquery
from gmail.rejects.rejects import Rejects
from datetime import datetime, timedelta
import os
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/proj.json"


class BigQ:

    def __init__(self):
        self.client = bigquery.Client()
        self.rejects = Rejects()
        self.rejects.addToRejectS(self.rejectDomains())

    def clean(self, s):
        return re.sub(r'\W+', ' ', s)

    def d(self, query="""
    SELECT a.* FROM `septapig.mail.mc` a
    left outer join `septapig.mail.parsed` b
    on a.id = b.id
    where b.id is null LIMIT 1000"""):
        return self.client.query(query).to_dataframe()

    def deleteBounce(self):
        query = "delete  FROM `septapig.mail.mc` " \
                "where returnpath like '%bounce%';"
        query_job = self.client.query(query)
        for row in query_job:
            # Row values can be accessed by field name or index.
            return row["now"]

    def deleteMsg(self, msg):
        query = "delete  FROM `septapig.mail.mc` " \
                "where msg like '%s';" % msg
        query_job = self.client.query(query)
        # return query_job.result()
        # FIXME: Can we call something else to run this?
        [x for x in query_job]
        return query_job

    def deleteMsgDays(self, msg, days=-1):
        FROM = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

        query = "delete  FROM `septapig.mail.mc` " \
                "where msg like '%s' and timeStamp >= '%s';" % (msg, FROM)
        query_job = self.client.query(query)
        [x for x in query_job]
        return query_job

    def rejectDomains(self):
        query = """
        select domain from `septapig.mail.reject_domain_p`
        """
        query_job = self.client.query(query)
        domains = []
        for row in query_job:
            # Row values can be accessed by field name or index.
            domains.append(row["domain"])
        return domains

    def createEML(self, limit=1):
        query = """
SELECT txt FROM `septapig.mail.parsed` 
where subject like '%C2C Contracts Only.%'
order by timeStamp desc
LIMIT {}
       """.format(limit)
        query_job = self.client.query(query)
        return query_job

    def getTime(self):
        query = "SELECT CURRENT_DATETIME('America/New_York') as now;"
        query_job = self.client.query(query)
        for row in query_job:
            # Row values can be accessed by field name or index.
            return row["now"]

    def select(self, query):
        query_job = self.client.query(query)
        return query_job

    def filter(self, returnpah):
        return self.rejects.returnpath(returnpah)

    def insert(self, id, ret, msg, raw, label=''):
        if self.filter(ret):
            return
        query = """
          insert into `septapig.mail.mc` (id,returnpath,msg,timeStamp, rawstr,
          label) 
          values ('%s','%s','%s','%s','%s','%s')
          """ % (id, ret, msg, self.getTime(), raw, label)

        query_job = self.client.query(query)
        [x for x in query_job]  # Make an API request.
        print("result:", query_job)
        return query_job

    def all_mesg_seen(self):
        query = """
        INSERT INTO `septapig.mail.reject_response`
            SELECT a.returnpath,a.timeStamp FROM `septapig.mail.response` a 
            left outer join   `septapig.mail.reject_response` b
            on a.returnpath=b.returnpath and a.timeStamp = b.timeStamp
            where b.returnpath is null
        """
