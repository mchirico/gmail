from __future__ import print_function
import pickle
import os.path
import warnings

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os
import pickle

from apiclient import errors

import logging
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/',
          'https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.settings.sharing']

TOPIC = 'projects/quickstart-1586788855488/topics/gmail-topic'


class Mail:
    data = []

    def __init__(self, service='default'):
        if service != 'default':
            self.service = self.getServiceDeadMail()
        else:
            self.service = self.getService()
            # self.watch(self.service)

    def pickle_it(self, file, obj):
        with open(file, 'wb') as f:
            pickle.dump(obj, f)

    def unpickle_it(self, file):
        with open(file, 'rb') as f:
            return pickle.load(f)

    def messageGet(self, userId,
                   id,
                   format='raw'):
        return self.service.users().messages().get(
            userId=userId,
            id=id,
            format=format).execute()

    def messageDelete(self, userId, id):
        return self.service.users().messages().delete(userId=userId,
                                                      id=id).execute()

    def messageList(self, label):
        return self.service.users() \
            .messages().list(userId='me',
                             labelIds=label).execute()

    def snippet(self, response, label=''):
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])
            for msg in messages:
                msg_id = msg['id']
                message = self.messageGet(
                    userId='me',
                    id=msg_id,
                    format='raw')
                print('\n\n --------------------- \n\n')
                print(message['snippet'])
                msg_str = base64.urlsafe_b64decode(
                    message['raw'].encode('ASCII'))
                msg_str = str(msg_str)
                try:
                    idx = str.index(msg_str, 'Return-Path:')
                    t = msg_str[idx:idx + 250]
                    idx2 = str.index(t, '\\r\\n')
                    reply = t[:idx2]

                except ValueError:
                    reply = 'not found'
                self.data.append([msg_id, reply, message['snippet'],
                                  msg_str[0:1500], message['raw'], label])
                self.messageDelete(userId='me',
                                   id=msg_id)

    def snippetDeadMail(self, response):
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])
            for msg in messages:
                msg_id = msg['id']
                message = self.service.users().messages().get(
                    userId='me',
                    id=msg_id,
                    format='minimal').execute()

                print(message['snippet'])

                if 'Test msg' in message['snippet']:
                    self.service.users().messages().delete(userId='me',
                                                           id=msg_id).execute()
                if 'Hope you are doing well!' in message['snippet']:
                    self.service.users().messages().delete(userId='me',
                                                           id=msg_id).execute()

    def watch(self, service):
        request = {
            'labelIds': ['INBOX'],
            'topicName': TOPIC
        }
        service.users().watch(userId='me', body=request).execute()

    def getService(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens,
        # and is
        # created automatically when the authorization flow completes for the
        # first
        # time.
        if os.path.exists('credentials/token.pickle'):
            with open('credentials/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('credentials/token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        return build('gmail', 'v1', credentials=creds)

    def getServiceDeadMail(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens,
        # and is
        # created automatically when the authorization flow completes for the
        # first
        # time.
        if os.path.exists('credentials/tokenDeadMail.pickle'):
            with open('credentials/tokenDeadMail.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('credentials/tokenDeadMail.pickle', 'wb') as token:
                pickle.dump(creds, token)

        return build('gmail', 'v1', credentials=creds)

    # TODO: Figure out how to close
    def close(self):
        pass

    def getListOfLabels(self):

        results = self.service.users().labels().list(userId='me').execute()

        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'], label['id'])

        return labels

    def populateSnippet(self):

        labelIds = ['INBOX', 'SPAM', 'TRASH', 'SENT']
        for label in labelIds:
            response = self.messageList(label)
            self.snippet(response, label)

        return self.getListOfLabels()

    def buildDeadLabels(self, tag='TEST'):
        labelIds = ['TRASH']
        r = self.getListOfLabels()
        add = [i['id'] for i in r if i['name'] == tag]
        for i in add:
            labelIds.insert(0, i)
        return labelIds

    def populateSnippetDeadMail(self):

        labelIds = self.buildDeadLabels('TEST')
        response = self.service.users().messages().list(userId='me',
                                                        labelIds=labelIds).execute()

        self.snippetDeadMail(response)
        return self.getListOfLabels()

    def create_message(self, sender, to, subject, message_text):
        """Create a message for an email.

        Args:
          sender: Email address of the sender.
          to: Email address of the receiver.
          subject: The subject of the email message.
          message_text: The text of the email message.

        Returns:
          An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {
            'raw':
                base64.urlsafe_b64encode(message.as_bytes()).decode('ascii')}

    def create_static_reply(self, message_text):
        """Create a message for an email.

        Args:
          sender: Email address of the sender.
          to: Email address of the receiver.
          subject: The subject of the email message.
          message_text: The text of the email message.

        Returns:
          An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = 'mchirico@gmail.com'
        thread = '<CAAuxAiicHMhSqr-KUeoXputgeRSO3TfKh6zvt=_voSgup0801g@mail' \
                 '.gmail.com>'
        message['In-Reply-To'] = thread
        message['from'] = 'me'
        message['subject'] = 'Re: test'
        return {
            'raw':
                base64.urlsafe_b64encode(message.as_bytes()).decode('ascii')}

    def send_message(self, service, user_id, message):
        """Send an email message.

        Args:
          service: Authorized Gmail API service instance.
          user_id: User's email address. The special value "me"
          can be used to indicate the authenticated user.
          message: Message to be sent.

        Returns:
          Sent Message.
        """
        try:
            message = (
                service.users().messages().send(userId=user_id,
                                                body=message).execute()
            )
            print('Message Id: %s' % message['id'])
            return message
        except errors.HttpError as error:
            print('An error occurred: %s' % error)


if __name__ == "__main__":
    print("here")
