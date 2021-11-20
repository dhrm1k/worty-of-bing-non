import flask
from replit import db, web
import json
import requests
from flask import Flask, redirect, url_for, request, send_from_directory
import os

app = flask.Flask(__name__)
app.static_url_path = "/static"


 
@app.route("/", methods=["GET", "POST"])
def index():
  thoughts = flask.request.form.get("thoughts")

  strthoughts = str(thoughts)

    
  entry = strthoughts
  if entry != "None" and len(entry) != 0:
    filename = 'posts.json'

      # 1. Read file contents
    with open(filename, "r") as file:
      data = json.load(file)
      #This code checks if the post inputted before and after is not the same. If it's the same, it will not get inserted.
      lenofall = len(data['thoughts'])

      if lenofall > 0: #0 cause 1 will look for second input.
        if data['thoughts'][0] != entry:
            data['thoughts'].insert(0, entry)
      else:
        data['thoughts'].insert(0, entry)

      # 3. Write json file
      with open(filename, "w") as file:
        json.dump(data, file)
  

  return flask.render_template('index.html', thoughts=thoughts)


@app.route("/api/feed")
def data():
  return flask.send_from_directory('', 'posts.json')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


web.run(app)

