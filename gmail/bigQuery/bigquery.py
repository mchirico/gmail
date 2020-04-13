from google.cloud import bigquery
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/proj.json"

class BigQ:

    def __init__(self):
        self.client = bigquery.Client()

    def insert(self,id,ret,msg):
        # Construct a BigQuery client object.

        id = id.replace("'", "~")
        ret = ret.replace("'", "~")
        msg = msg.replace("'", "~")

        query = """
          insert into `septapig.mail.mc` (id,returnpath,msg) 
          values ('%s','%s','%s')
          """ % (id,ret,msg)

        query_job = self.client.query(query)  # Make an API request.
        print("result:",query_job)




