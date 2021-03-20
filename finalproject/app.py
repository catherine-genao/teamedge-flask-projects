from flask import Flask, redirect,render_template, url_for, request
from sense_emu import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep
sense = SenseHat()
app = Flask(__name__)

@app.route('/message')
def index():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/success', methods=['GET','POST'])
def success():
   message = request.form['message']
   sense.show_message(message)
   return render_template('success.html', message = message)

if __name__ == '__main__':
      app.run(debug=True, host='127.0.0.4')