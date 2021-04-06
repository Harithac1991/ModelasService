model = None
import joblib
import numpy as np 
from flask import Flask,request
import os 
 
app = Flask(__name__)
def load_model():
	global model
	model = joblib.load( "forest_reg.pkl")


@app.route("/")  # app.route is a decorator
def home():
	return "Welcome to Housing price prediction"

@app.route("/predict", methods=["POST"])
def get_pred():
	if request.method=="POST":
		data = request.get_json()["input"]
		# data = [-1.17,0.65,-1.16,-0.90,-1.03,-0.99,-1.022,1.336,0.217,-0.03,1,0,0,0,0]
		data = np.array(data)[np.newaxis, :] 		
		pred = model.predict(data)
	return str(pred[0])

# @app.route("/predict", methods=["POST"])
# def get_pred():
# 	return ("Predicted values to be displayed")


if __name__ == '__main__':
	load_model()
	app.run(host='localhost', port=8000, debug=True)



