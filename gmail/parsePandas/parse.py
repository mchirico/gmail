import base64
import email.utils
import warnings
from datetime import datetime
import time


class Parse:
    d = None

    def __init__(self, d):
        self.d = d

    def raw(self):
        self.d['txt'] = self.d['rawstr'].apply(
            lambda x: base64.urlsafe_b64decode(
                x.encode('ASCII')))
        return self

    def subject(self):
        def extractSubject(b):
            try:
                tag = '\r\nSubject:'
                b = b.decode()
                idx = str.index(b, tag)
                b = b[idx + len(tag) + 1:idx + 500].strip()
                idx2 = str.index(b, '\r\n')
            except:
                return 'none'
            return b[0:idx2]

        self.d['subject'] = self.d['txt'].apply(lambda x: extractSubject(x))
        return self

    def messageID(self):
        def extractMessageID(b):
            try:
                tag = '\r\nMessage-ID:'
                b = b.decode()
                idx = str.index(b, tag)
                b = b[idx + len(tag) + 1:idx + 500].strip()
                idx2 = str.index(b, '\r\n')
            except:
                return 'none'
            return b[0:idx2]

        self.d['messageID'] = self.d['txt'].apply(lambda x: extractMessageID(x))
        return self

    def date(self):
        def extractDate(b):
            try:
                tag = '\r\nDate:'
                b = b.decode()
                idx = str.index(b, tag)
                b = b[idx + len(tag) + 1:idx + 500].strip()
                idx2 = str.index(b, '\r\n')
                pd = email.utils.parsedate(b[0:idx2])
                b = datetime.fromtimestamp(time.mktime(pd)).strftime(
                    "%Y-%m-%dT%H:%M:%S.%s")

            except:
                return 'none'
            return b

        self.d['date'] = self.d['txt'].apply(lambda x: extractDate(x))
        return self

    def received(self):
        def extractReceived(b):
            try:
                tag = '\r\nReceived:'
                b = b.decode()
                idx = str.index(b, tag) + 10
                # We want 2nd
                b = b[idx::]
                idx = str.index(b, tag)
                b = b[idx + len(tag) + 1:idx + 500].strip()
                idx2 = str.index(b, '\r\n')
            except:
                return 'none'
            return b[0:idx2]

        self.d['received'] = self.d['txt'].apply(lambda x: extractReceived(x))
        return self

    def save(self):
        #  `septapig.mail.mc` LIMIT
        warnings.simplefilter("ignore")
        self.d.to_gbq('mail.tmp0', project_id='septapig', if_exists='replace')
