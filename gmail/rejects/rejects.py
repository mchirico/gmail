import re
from gmail.rejects.listing import rejects


class Rejects:
    mylist = ['found', 'human', 'reject', '<>', 'deegit.com',
              'tech.com', 'mail.net', 'talent', 'solutions',
              'apolisrises.com', 'sparkpost.com', 'beyond.com', 'patel',
              'solutions.com', 'smtp.com', 'kumar', 'salesforce.com',
              'providers.com', 'spectrum.com', 'kodus.com', 'sparkpost.com',
              'indeed.com', 'bounce', 'job.com', 'assessment','compuvis.com',
              'municipalnotices.com','yahoo.com','postmaster','alert',
              'e-notify','indeedemail.com','nlbservices.com',
              'techaffinity.com','eblank','experthiring.com',
              'kellyit.com','v2soft.com','damcosoft.com','kmail.com','smtp',
              'email','cwxstat.com@','infosmartsys.com','7','6','4','9',
              '0','8']

    def match(self, returnpath):
        m = re.search(r"(@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", returnpath)
        return m

    def returnpath(self, returnpath):
        for i in self.mylist:
            if i in str(returnpath).lower():
                return True
            m = self.match(returnpath)
            if m:
                if m.group(0) in rejects:
                    return True
        return False
