from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app=application

## Import Lasso CV and Standard scalar pickle files
path = 'C:\\Users\\pc\\PycharmProjects\\PythonProject\\First_ML_project\\models'
lassoCV_model = pickle.load(open(f'{path}\\lassoCV.pkl', 'rb'))
scaler = pickle.load(open(f'{path}\\scalar.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoints():
    if request.method=="POST":
        Temperature = float(request.form.get('temp'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('ws'))
        Rain = float(request.form.get('rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_scaler_data = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = lassoCV_model.predict(new_scaler_data) #This will return a list with one element

        return render_template('home.html', results=result[0])

    else:
        return render_template('home.html')

if __name__=='__main__':
    app.run(host="0.0.0.0")