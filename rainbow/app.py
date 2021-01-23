from flask import Flask, render_template, current_app as app


app = Flask(__name__)

@app.route('/')
def index():
 return "welcome to Catherine's rainbow app!"

@app.route('/red')
def red():
    name = "red"
    background = "red"
    return render_template('rainbow.html', name = name, background = background)


@app.route('/orange')
def orange():
    name = "orange"
    background = "orange"
    return render_template('rainbow.html', name = name, background = background)

@app.route('/yellow')
def yellow():
    name = "yellow"
    background = "yellow"
    return render_template('rainbow.html', name = name, background = background)




@app.route('/green')
def green():
    name = "green"
    background = "green"
    return render_template('rainbow.html', name = name, background = background)


@app.route('/blue')
def blue():
   name = "blue"
   background = "blue"
   return render_template('rainbow.html', name = name, background = background)


@app.route('/purple')
def purple():
    name = "purple"
    background = "#4F2F4F"
    return render_template('rainbow.html', name = name, background = background)



if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
