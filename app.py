import requests
import json
import pprint
from collections import OrderedDict
import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
import datetime

app = Flask(__name__)

DATA = ""
CAN_ENTER = 0

# initializes values for link and API Key
url = "https://servers.pixelplus.nl/api/v1/servers?"
parameter = {"token":"ZBuwzQqlxQUIWwEbtooWYSPPmdfjnGMU"}


# initializes response
response = requests.get(url, parameter)


# Writes data to data.txt in current directory
if response.status_code == 200:
    with open("data.txt", "w") as file:
        data = json.loads(response.text)
        DATA = data
        file.write((pprint.pformat(data)))
else:
    print(f"Error {response.status_code}")


with open("temp_key_values.txt", "w") as file:
    server_data = data['data'][0]
    unique_keys = list(OrderedDict.fromkeys(server_data))
    for key in unique_keys:
        file.write(key + '\n')


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


def timestamp_to_string(timestamp):
    if timestamp is None:
        return None
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    dt_string = dt_object.strftime("%Y-%m-%d %H:%M:%S")
    return str(dt_string)

@app.route("/", methods=["GET", "POST"])
def display():
    if request.method == "POST":
        password = request.form.get("password")
        if not password:
            return
        elif password == "white rabbit":
            return redirect("/enter")
        else:
            return render_template("enter.html", error="Invalid password.")
    else:
        return render_template("enter.html")


@app.route("/enter", methods=["GET", "POST"])
def enter():
    password = request.form.get("password")
    if password != "white rabbit":
        return render_template("enter.html", error="Invalid password.")
    else:
        return render_template("layout.html", data=DATA)


@app.context_processor
def inject_functions():
    return dict(timestamp_to_string=timestamp_to_string)


app.jinja_env.globals.update(enumerate=enumerate)
