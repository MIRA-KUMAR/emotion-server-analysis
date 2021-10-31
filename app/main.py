import json

from flask import Flask, request, Response


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return {"name": "fizan"}




