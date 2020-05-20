import firebase_admin
from firebase_admin import credentials, firestore
import os.path

from utils.util import findFile
import time
import datetime

import threading

os.environ['TZ'] = 'US/Eastern'
time.tzset()

cred = credentials.Certificate(findFile("firebase.json"))
firebase_admin.initialize_app(cred)
db = firestore.client()


class FBmail:

    def delete(self, id):
        db.collection(u'gmail').document(
            'possible').collection(
            'summary').document(str(id)).delete()

    def update(self, count, subject, returnpath, msg,
               timeStamp):
        now = datetime.datetime.now()
        rectimeStamp = now.strftime("%Y-%m-%dT%H:%M:%S.%s")
        timeStamp_epoch = now.timestamp()
        doc_ref = db.collection(u'gmail').document(
            'possible').collection(
            'summary').document(str(count))
        doc_ref.set({
            u'id': str(count),
            u'subject': str(subject),
            u'returnpath': str(returnpath),
            u'msg': str(msg),
            u'timeStampS': timeStamp.strftime("%Y-%m-%d %H:%M:%S"),
            u'timeStamp': timeStamp,
            u'rectimeStamp': rectimeStamp,
            u'timeStamp_epoch': timeStamp_epoch
        })

    def event(self, callback_done, mylog):
        # Create a callback on_snapshot function to capture changes
        def on_snapshot2(doc_snapshot, changes, read_time):
            for doc in doc_snapshot:
                print(u'Received document snapshot: {}'.format(doc.id))
                mylog(u'test1 document snapshot: {}'.format(doc.to_dict()))
                # mylog(u'\n     changes: {}\n read_time: {}'.format(dir(
                # changes),
                #                                                  read_time))
                callback_done.set()

        doc_ref = db.collection(u'event').document(u'chirico')

        # Watch the document
        doc_watch = doc_ref.on_snapshot(on_snapshot2)
        return doc_watch
        # doc_watch.unsubscribe()
