from google.cloud import bigquery
import os
import time
from utils.util import findFile
# Imports the Google Cloud client library
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = findFile("proj.json")
os.environ['TZ'] = 'US/Eastern'
time.tzset()

BUCKET = "gmailmc"


class Buckets:

    def create(self):
        # Instantiates a client
        storage_client = storage.Client()
        bucket_name = BUCKET
        bucket = storage_client.create_bucket(bucket_name)
        print("Bucket {} created.".format(bucket.name))

    def createFromString(self, file, data):
        client = storage.Client()
        bucket = client.get_bucket(BUCKET)

        blob = bucket.blob(file)
        blob.upload_from_string(data)

    def readFromString(self, file):
        client = storage.Client()
        bucket = client.get_bucket(BUCKET)

        blob = bucket.blob(file)
        data = blob.download_as_string()
        return data

    def upload(self):
        client = storage.Client()
        bucket = client.get_bucket(BUCKET)

        blob = bucket.blob('file.txt')
        blob.upload_from_string('New contents!')
        files = [x.name for x in bucket.list_blobs()]
        return files

    def list(self,prefix=''):
        client = storage.Client()
        bucket = client.get_bucket(BUCKET)
        files = [x.name for x in bucket.list_blobs(prefix=prefix)]
        return files
