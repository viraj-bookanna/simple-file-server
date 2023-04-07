import os
from flask import Flask,request,send_from_directory

app = Flask(__name__)

@app.route('/files/', methods = ['GET'])
def list_files():
    retval = ''
    for item in os.scandir(os.getcwd()):
        if item.is_file():
            retval += '<a href="/file/{}"></a><br>'.format(item.name)
    return retval
@app.route('/file/<filename>', methods = ['GET'])
def getfile(filename):
    return send_from_directory(os.getcwd(), filename)