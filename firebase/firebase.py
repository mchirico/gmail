import firebase_admin
from firebase_admin import credentials, firestore
import os.path

from utils.util import findFile
import time
import datetime

os.environ['TZ'] = 'US/Eastern'
time.tzset()

cred = credentials.Certificate(findFile("firebase.json"))
firebase_admin.initialize_app(cred)
db = firestore.client()


class FBmail:

    def delete(self,id):
        db.collection(u'gmail').document(
            'possible').collection(
            'summary').document(str(id)).delete()



    def update(self, id, msg, date):
        now = datetime.datetime.now()
        timeStamp = now.strftime("%Y-%m-%dT%H:%M:%S.%s")
        timeStamp_epoch = now.timestamp()
        doc_ref = db.collection(u'gmail').document(
            'possible').collection(
            'summary').document(str(id))
        doc_ref.set({
            u'id': str(id),
            u'msg': str(msg),
            u'date': str(date),
            u'timeStamp': timeStamp,
            u'timeStamp_epoch': timeStamp_epoch
        })
