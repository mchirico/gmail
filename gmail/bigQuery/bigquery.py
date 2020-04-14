from google.cloud import bigquery
import os
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/proj.json"


class BigQ:

    def __init__(self):
        self.client = bigquery.Client()

    def clean(self, s):
        return re.sub(r'\W+', ' ', s)

    def getTime(self):
        query = "SELECT CURRENT_DATETIME('America/New_York') as now;"
        query_job = self.client.query(query)
        for row in query_job:
            # Row values can be accessed by field name or index.
            return row["now"]

    def insert(self, id, ret, msg, raw):
        id = self.clean(id)
        msg = self.clean(msg)

        query = """
          insert into `septapig.mail.mc` (id,returnpath,msg,timeStamp, rawstr) 
          values ('%s','%s','%s','%s','%s')
          """ % (id, ret, msg,self.getTime(),raw)

        query_job = self.client.query(query)  # Make an API request.
        print("result:", query_job)
