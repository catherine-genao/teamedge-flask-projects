from flask import Flask, redirect,render_template, url_for, request
from sense_hat import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep
sense = SenseHat()
app = Flask(__name__)

@app.route('/message')
def index():
    return render_template('message.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST' ])
def login():
   
   if request.method == 'POST':
      user = request.form['name']
      message = request.form['message']
      sense.show_message(message)
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('name')
      return redirect(url_for('success',name = user))


if __name__ == '__main__':
      app.run(debug=True, host='127.0.0.1')