from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/friends')
def index():
    friends = ["catherine", "owllette", "cynclara", "bob"]
    return render_template('rainbow.html', friends = friends)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
