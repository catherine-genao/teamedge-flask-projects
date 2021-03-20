from sense_hat import SenseHat
from flask import Flask, render_template, request, current_app as app
import os
import requests

app = Flask(__name__)

@app.route('/message')
def  index():


    return render_template('message.html')

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0' )