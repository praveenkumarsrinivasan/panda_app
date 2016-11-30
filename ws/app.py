#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 praveenkumarsrinivasan <praveen.sxi@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

from flask import Flask
from flask_cors import CORS
from random import randint
import socket, json

app = Flask(__name__)
cors = CORS(app, resources={r"/words/*": {"origins": "*"}})

@app.route('/words/')
def index():
    return 'Hello World'

@app.route('/words/noun')
def noun():
    nouns = ["dead body", "elephant", "go language", "laptop", "container", "micro-service", "turtle", "whale"]
    res = {}
    res['word'] = nouns[randint(0,len(nouns)-1)]
    res['hostname'] = socket.gethostname()
    return json.dumps(res)

@app.route('/words/verb')
def verb():
    verbs = ["will drink", "smashes", "smokes", "eats", "walks towards", "loves", "helps", "pushes", "debugs"]
    res = {}
    res['word'] = verbs[randint(0,len(verbs)-1)]
    res['hostname'] = socket.gethostname()
    return json.dumps(res)

@app.route('/words/adjectives')
def adjectives():
    adjectives = ["the exquisite", "a pink", "the rotten", "a red", "the floating", "a broken", "a shiny", "the pretty", "the impressive", "an awesome"]
    res = {}
    res['word'] = adjectives[randint(0,len(adjectives)-1)]
    res['hostname'] = socket.gethostname()
    return json.dumps(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

