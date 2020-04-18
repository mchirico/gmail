from google.cloud import bigquery
import os
import re

import requests
import pandas as pd
import numpy as np
from datetime import datetime

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/proj.json"


class BigQ:

    def __init__(self):
        self.client = bigquery.Client()

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

    def getTime(self):
        query = "SELECT CURRENT_DATETIME('America/New_York') as now;"
        query_job = self.client.query(query)
        for row in query_job:
            # Row values can be accessed by field name or index.
            return row["now"]

    def select(self, query):
        query_job = self.client.query(query)
        return query_job

    def insert(self, id, ret, msg, raw, label=''):
        query = """
          insert into `septapig.mail.mc` (id,returnpath,msg,timeStamp, rawstr,
          label) 
          values ('%s','%s','%s','%s','%s','%s')
          """ % (id, ret, msg, self.getTime(), raw, label)

        query_job = self.client.query(query)
        [x for x in query_job]  # Make an API request.
        print("result:", query_job)
        return query_job
