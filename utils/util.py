import pickle
from os import path


def pickle_it(file, obj):
    with open(file, 'wb') as f:
        pickle.dump(obj, f)


def unpickle_it(file):
    with open(file, 'rb') as f:
        return pickle.load(f)


def findFile(file="bigquery.json"):
    if path.exists("credentials/{}".format(file)):
        return "credentials/{}".format(file)
    if path.exists("../credentials/{}".format(file)):
        return "../credentials/{}".format(file)
    if path.exists("/credentials/{}".format(file)):
        return "/credentials/{}".format(file)
    if path.exists("etc/strava/credentials/{}".format(file)):
        return "etc/strava/credentials/{}".format(file)
