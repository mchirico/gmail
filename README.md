![Cloud Build](https://github.com/mchirico/gmail/workflows/Cloud%20Build/badge.svg?branch=master)
![Schedule Build](https://github.com/mchirico/gmail/workflows/Schedule%20Build/badge.svg)
[![codecov](https://codecov.io/gh/mchirico/gmail/branch/master/graph/badge.svg)](https://codecov.io/gh/mchirico/gmail)
[![codebeat badge](https://codebeat.co/badges/6a7f697e-058f-468d-9475-6551f5d9f0c6)](https://codebeat.co/projects/github-com-mchirico-gmail-master)
# Gmail

Project to read and filter gmail messages

<img src='https://storage.googleapis.com/montco-stats/gmail/ActivityDiagramGmail.svg' />

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


You'll need to run the quickstart, afer delete *token.pickle* in credentials

[quickstart](https://gist.github.com/mchirico/3916cb132c27e99262baf6f87e9ffcae)

Note: Quickstart is one of *my* projects.

Note... quickstart is my project.
![image](https://user-images.githubusercontent.com/755710/87828738-91a78a00-c84b-11ea-8e19-5bb736302d92.png)


