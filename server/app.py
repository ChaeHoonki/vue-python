from flask import Flask, jsonify
from flask_cors import CORS
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QAxContainer import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/login', methods=['GET'])
def login():
    ap = QMainWindow()
    ap.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

    return jsonify('success!')


if __name__ == '__main__':
    app.run()
