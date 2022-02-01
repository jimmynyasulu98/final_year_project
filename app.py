import threading
from flask import Flask
import requests
import time

app = Flask(__name__)


@app.route('/')
def index():
    return ''


@app.route('/door_stats')
def door_stats():
    return


@app.route('/graphs')
def graph_plot():
    return


if __name__ == '__main__':
    updates = threading.Thread(target=None, args=(1,))
    updates.start()
    app.run(debug=True, threaded=True)
