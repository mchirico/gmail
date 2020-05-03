import os
import threading
import atexit
from gmail.bigQuery.bigquery import BigQ

from flask import Flask, make_response, render_template, send_from_directory

from gmail.pubsub.pubsub import PubSub

POOL_TIME = 30  # Seconds

# variables that are accessible from anywhere
commonDataStruct = 0
# lock to control access to variable
dataLock = threading.RLock()
# thread handler
yourThread = threading.Thread()


def create_app():
    app = Flask(__name__)
    angular_folder = os.path.join(app.root_path, 'templates')

    @app.route('/<path:filename>')
    def angular(filename):
        return send_from_directory(angular_folder, filename)

    @app.route('/')
    def index():
        resp = make_response(render_template('index.html'))
        return resp

    def interrupt():
        global yourThread
        yourThread.cancel()

    def doStuff():
        global commonDataStruct
        global yourThread
        with dataLock:
            commonDataStruct += 1
            p = PubSub()
            p.send()
            p.readMsgProcess(POOL_TIME - 2)
        # Set the next thread to happen
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    def doStuffStart():
        # Do initialisation stuff here
        global yourThread
        # Create your thread
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    # Initiate
    # doStuffStart()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
