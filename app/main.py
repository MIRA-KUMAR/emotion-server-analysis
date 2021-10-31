import json
import pickle

from flask import Flask, request, Response

with open("dict.pickle", "rb") as f:
    vectorizer = pickle.load(f)

with open("rfc.pickle", "rb") as f:
    rfc = pickle.load(f)

with open("svc.pickle", "rb") as f:
    svc = pickle.load(f)

with open("lsvc.pickle", "rb") as f:
    lsvc= pickle.load(f)

with open("dtc.pickle", "rb") as f:
    dtc= pickle.load(f)


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return {"name": "fizan"}

@app.route("/predict", methods=["POST"])
def predict():
    body = request.get_json()       #{text: "Tom is a good boy", model: "RFC"}
    vectorized_body= vectorizer.transform(body.text)
    if body.model =="RFC":
        prediction = rfc.predict(vectorized_body)
        return prediction[0]
    if body.model =="SVC":
        prediction = svc.predict(vectorized_body)
        return prediction[0]
    if body.model =="LSVC":
        prediction = lsvc.predict(vectorized_body)
        return prediction[0]
    
    prediction = dtc.predict(vectorized_body)
    return prediction[0]




