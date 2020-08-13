from gmail.bigQuery.bigquery import BigQ
from gmail.mail.extract_eml import cleanBinaryEmail
from gmail.mail.mail import Mail
from gmail.storage.storage import Buckets


class Analyze:

    def queryParsedEMLnoTXT(self, limit=1):
        b = BigQ()
        query = """
        SELECT subject,msg,timeStamp,returnpath FROM `septapig.mail.parsed` 
        where subject like '%C2C Contracts Only.%'
        and timeStamp > (select max(timestamp) from `septapig.mail.analysis`)
        order by timeStamp desc
        LIMIT {}
               """.format(limit)
        return b.select(query)

    def queryParsedEML(self, limit=1):
        b = BigQ()
        query = """
        SELECT txt,subject,msg,timeStamp,returnpath FROM `septapig.mail.parsed` 
        where subject like '%C2C Contracts Only.%'
        and timeStamp > (select max(timeStamp) from `septapig.mail.analysis`)
        order by timeStamp desc
        LIMIT {}
               """.format(limit)
        return b.select(query)

    def updateAnalysisTable(self, stored_file):
        b = BigQ()
        query = """
        insert into `septapig.mail.analysis` (txt,subject,msg,timeStamp,
        returnpath,stored_file)
          SELECT txt,subject,msg,timeStamp,returnpath,'{}' FROM 
          `septapig.mail.parsed` 
          where subject like '%C2C Contracts Only.%'
        and timeStamp > (select max(timeStamp) from `septapig.mail.analysis`)
        """.format(stored_file)
        query_job = b.select(query)
        [x for x in query_job]
        return query_job

    def analyzeStatus(self, limit=1):
        row = self.queryParsedEMLnoTXT(5)
        timeStamp = [c['timeStamp'] for c in row]
        msg = [c['msg'] for c in row]
        returnpath = [c['returnpath'] for c in row]
        return (timeStamp, returnpath, msg)

    def emailAlert(self, to, msg):
        m = Mail()
        service = m.getService()
        message = m.create_message('mc@cwxstat.com',
                                   to,
                                   'C2C Agree',
                                   msg)
        id = m.send_message(service, 'me', message)
        return id

    def analyzeEML(self, limit=1):
        row = self.queryParsedEML(1)
        txtEMLs = [c['txt'] for c in row]
        timeStamp = [c['timeStamp'] for c in row]
        txt = [c['timeStamp'] for c in row]
        returnpath = [c['returnpath'] for c in row]
        msg = [c['msg'] for c in row]
        return (timeStamp, txtEMLs, txt, returnpath, msg)

    def writeEML(self, txtEMLs, files):
        b = Buckets()
        for file, raw_email in zip(files, txtEMLs):
            email = cleanBinaryEmail(raw_email)
            b.createFromString(file, email)
