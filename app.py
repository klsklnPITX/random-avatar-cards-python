from flask import Flask, render_template, url_for
import json

app = Flask(__name__)


def get_avatars():
    with open("static/avatar.json") as f:
        data_avatars = json.load(f)
    return data_avatars


@app.route("/")
def index():
    data_avatars = get_avatars()
    return render_template("index.html", data_avatars=data_avatars)
