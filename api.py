from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
from flask_cors import CORS
#import pickle as p
import json
import tensorflow as tf
import requests
from tensorflow import keras


global model
modelfile = './tempmodel.h5'
model = tf.keras.models.load_model(modelfile)

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

def parseData(data):
    # temp = json.loads(data)
    # print(temp)
    lst = []
    for key, value in data.items():
        lst.append(float(value))
    print(lst)
    return [lst]

@app.route('/', methods=['GET','POST'])
def makecalc():
    print("inside mackecalc")
    response_object={'status':'success'}
    print(request.method)
    if (request.method=='POST'):
        print("inside the if")
        data = request.get_json(force=True)
        new = parseData(data)
        prediction = np.array2string(model.predict(new))
        print(prediction)
        if(str(prediction)=="[[1.]]"):
            print("inner if")
            response_object=json.dumps({'status':'1'})
        elif(str(prediction)=="[[0.]]"):
            response_object={'status':'0'}
    return response_object


# sanity check route


if __name__ == '__main__':
    #model = p.load(open(modelfile, 'rb'))
    print(modelfile)
    print(model)
    app.run() 