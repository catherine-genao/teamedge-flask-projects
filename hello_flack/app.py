from flask  import Flask, render_template
from datatime import date
import requests

app = Flask(__name__)

@app.route('/')
def index():
   name "Catherine"
   group_name= ['Tiana','Cooper','Catherine' 'Richlove' ]
   return render_template('index.html', greeting=name, group=group)
 @app.route('/richlove')
 def Richlove():
     return render_template('richlove.html')


@app.route('/nasa')
def show_nasa_pic():
    today = str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
    data = response.json()
    return render_template('nasa.html',data=data)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
     
