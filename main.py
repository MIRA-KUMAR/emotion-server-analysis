import json

from flask import Flask, request, Response


app = Flask('fff')

@app.route("/", methods=["GET"])
def index():
    return {"name": "fizan"}



if __name__ == '__main__':
    app.run()
