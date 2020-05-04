![Cloud Build](https://github.com/mchirico/gmail/workflows/Cloud%20Build/badge.svg?branch=master)
![Schedule Build](https://github.com/mchirico/gmail/workflows/Schedule%20Build/badge.svg)
[![codecov](https://codecov.io/gh/mchirico/gmail/branch/master/graph/badge.svg)](https://codecov.io/gh/mchirico/gmail)
# Gmail

Project to read and filter gmail messages

```
# See Makefile
docker pull gcr.io/septapig/gmail



# Topics and Subs
# Project: quickstart-1586788855488
gcloud pubsub topics create gmail-topic
gcloud pubsub subscriptions create gmail-sub --topic gmail-topic

# Note pytest actually delete's emails...

references:
https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-python

```


