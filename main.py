import flask
from replit import db, web
import json

app = flask.Flask(__name__)
app.static_url_path = "/static"


 
@app.route("/", methods=["GET", "POST"])
def index():
  thoughts = flask.request.form.get("thoughts")

  strthoughts = str(thoughts)

    
  entry = strthoughts

  

  filename = 'posts.json'


  # 1. Read file contents
  with open(filename, "r") as file:
    data = json.load(file)
    data.append(entry)

# 3. Write json file
  with open(filename, "w") as file:
    json.dump(data, file)

  

  return flask.render_template('index.html', thoughts=thoughts)


@app.route("/api/feed")
def data():
  return flask.send_from_directory('', 'posts.json')

web.run(app)

