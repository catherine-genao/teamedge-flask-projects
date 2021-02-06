from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests


app = Flask(__name__)

@app.route('/api/v2/holiday')
def pic():
	response = requests.get('https://date.nager.at/api/v2/PublicHolidays/2021/US')
	data = response.json()
	
	print (data)
	return render_template('holiday.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
