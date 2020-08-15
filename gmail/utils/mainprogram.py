from gmail.analysis.analyze import Analyze
from gmail.bigQuery.bigquery import BigQ
from gmail.mail.mail import Mail
from gmail.parsePandas.parse import Parse


def UpdateTableParsed():
    b = BigQ()
    # b.select('drop table IF EXISTS `septapig.mail.tmp0`')

    d = b.d()
    p = Parse(d)
    p.raw().subject().date().received().save()
    query = """
            insert into  `septapig.mail.parsed` 
    SELECT b.* FROM `septapig.mail.parsed` a
    right outer join `septapig.mail.tmp0` b
    on a.id = b.id
    where a.id is null
            """
    result = b.select(query)
    [x for x in result]


def insertTableMC():
    m = Mail()
    q = BigQ()
    m.populateSnippet()
    for i in m.data:
        q.insert(i[0], i[1], i[2], i[4], i[5])


def cleanUpBadEmails():
    q = BigQ()
    q.deleteMsgDays('%Hope you are doing well%')
    q.deleteMsgDays('%Test msg delete*%')
    q.delete100dayOld()


def runAnalytics():
    a = Analyze()
    a.runAnalyze()


def MainProcess():
    insertTableMC()
    UpdateTableParsed()
    cleanUpBadEmails()
    runAnalytics()
