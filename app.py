import os
from flask import Flask,request,send_from_directory

app = Flask(__name__)

@app.route('/file/<filename>', methods = ['GET'])
def getfile(filename):
    return send_from_directory(os.getcwd(), filename)