from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import requests
import pickle
app= Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction')
def predication(prediction):
    return predication

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        item_mrp = float(request.form['item_mrp'])
        outlet_identifier = request.form['outlet_identifer']
        if outlet_identifier == 'OUT027':
            outlet_identifier_out027 = 1
            outlet_identifier_out019 = 0
        elif outlet_identifier == 'OUT019':
            outlet_identifier_out027 = 0
            outlet_identifier_out019 = 1
        else:
            outlet_identifier_out027 = 0
            outlet_identifier_out019 = 0
        outlet_type = request.form['outlet_type']
        if outlet_type == 'Supermarket Type1':
            outlet_type_spt1 = 1
            outlet_type_spt3 = 0
        elif outlet_type == 'Supermarket Type3':
            outlet_type_spt1 = 0
            outlet_type_spt3 = 1
        else:
            outlet_type_spt1 = 0
            outlet_type_spt3 = 0
        outlet_size = request.form['outlet_size']
        if outlet_size == "Small":
            outlet_size_s = 1
            outlet_size_m = 0
            outlet_size_n = 0
        elif outlet_size == "Medium":
            outlet_size_s = 0
            outlet_size_m = 1
            outlet_size_n = 0
        elif outlet_size == "NaN":
            outlet_size_s = 0
            outlet_size_m = 0
            outlet_size_n = 1
        else:
            outlet_size_s = 0
            outlet_size_m = 0
            outlet_size_n = 0
        item_visibility = float(request.form['item_visibility'])
        scaled = scaler.transform(np.array([item_mrp,outlet_identifier_out027,outlet_type_spt3,outlet_identifier_out019,outlet_size_m,outlet_size_n,item_visibility,outlet_type_spt1,outlet_size_s]).reshape(1, -1))
        prediction = model.predict(scaled)[0]
    return redirect(url_for('prediction'))

if __name__=='__main__':
    app.run(debug=True)
