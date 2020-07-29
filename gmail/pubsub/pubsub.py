import os
from google.cloud import pubsub_v1
from gmail.bigQuery.bigquery import BigQ

# TODO project_id = "Your Google Cloud Project ID"
# TODO topic_name = "Your Pub/Sub topic name"
from gmail.mail.mail import Mail

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/proj.json"
# projects/quickstart-1586788855488/topics/gmail-topic
PROJECT = 'quickstart-1586788855488'
TOPIC = 'gmail-topic'
SUB = 'gmail-sub'


class PubSub:
    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_name}`
    topic_path = publisher.topic_path(PROJECT, TOPIC)
    subscriber = pubsub_v1.SubscriberClient()

    subscription_path = subscriber.subscription_path(
        PROJECT, SUB
    )

    def send(self):
        for n in range(1, 2):
            data = u"Message number {}".format(n)
            # Data must be a bytestring
            data = data.encode("utf-8")
            # When you publish a message, the client returns a future.
            future = self.publisher.publish(self.topic_path, data=data)
            print(future.result())

        print("Published messages.")

    def read(self, timeout):

        # The `subscription_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/subscriptions/{subscription_name}`

        def callback(message):
            print("Received message: {}".format(message))
            message.ack()

        streaming_pull_future = self.subscriber.subscribe(
            self.subscription_path, callback=callback
        )
        print("Listening for messages on {}..\n".format(self.subscription_path))

        # Wrap subscriber in a 'with' block to automatically call close()
        # when done.
        with self.subscriber:
            try:
                # When `timeout` is not set, result() will block indefinitely,
                # unless an exception is encountered first.
                streaming_pull_future.result(timeout=timeout)
            except:  # noqa
                streaming_pull_future.cancel()

    def readMsgProcess(self, timeout):

        def callback(message):
            m = Mail()
            q = BigQ()
            m.populateSnippet()
            for i in m.data:
                q.insert(i[0], i[1], i[2], i[4])
            print("Received message: {}".format(message))
            message.ack()

        streaming_pull_future = self.subscriber.subscribe(
            self.subscription_path, callback=callback
        )
        print("Listening for messages on {}..\n".format(self.subscription_path))

        # Wrap subscriber in a 'with' block to automatically call close()
        # when done.
        with self.subscriber:
            try:
                # When `timeout` is not set, result() will block indefinitely,
                # unless an exception is encountered first.
                streaming_pull_future.result(timeout=timeout)

            except:  # noqa
                streaming_pull_future.cancel()

