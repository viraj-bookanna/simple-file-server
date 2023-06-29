import os
from flask import Flask,request,send_from_directory
from dotenv import load_dotenv

load_dotenv(override=True)

SERVER_ROOT = os.getenv("SERVER_ROOT", os.getcwd())

app = Flask(__name__)

@app.route('/files/', methods = ['GET'])
def list_files():
    retval = ''
    for item in os.scandir(SERVER_ROOT):
        if item.is_file():
            retval += f'<a href="/file/{item.name}">{item.name}</a><br>'
    return retval
@app.route('/file/<filename>', methods = ['GET'])
def getfile(filename):
    return send_from_directory(SERVER_ROOT, filename)

if __name__ == '__main__':
    app.run()