from flask import Flask, render_template, request
import os
from mlProject.pipeline import prediction
import numpy as np
import cv2


app = Flask(__name__)

@app.route("/",methods=['GET'])
def homePage():
    return render_template("index2.html")


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)