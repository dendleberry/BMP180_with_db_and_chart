#!/usr/bin/python3
from flask import Flask, render_template, request

import mysql.connector as mariadb
import datetime
import db
import os
import random
import json

app = Flask(__name__)

@app.route("/")
def hello():
   templateData = {
      'title' : 'Sweet Sewer App'
   }
   return render_template('index.html', **templateData)

@app.route("/start")
def start():
   db.start_reading()
   return 'Stopped if youre seeing this'

@app.route("/stop")
def stop():
   db.stop_reading()
   return 'Stopped'

@app.route("/get")
def get():
   if request.args:
      fromDate = request.args.get('from')
      toDate = request.args.get('to')
   else:
      fromDate = ''
      toDate = ''
   labels, data = db.get_data(fromDate, toDate)
   response = {"labels": labels, "data": data}
   y = json.dumps(response, default=str)
   return y

if __name__ == "__main__":
   os.system('hostname -I')
   app.run(host='0.0.0.0', port=80, debug=True)
