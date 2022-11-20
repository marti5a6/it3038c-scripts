from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='', static_folder='./static', template_folder='./templates')
app.config.from_object(__name__)

@app.route('/')
def hello():
    # name = 'Tony'
    return render_template("index.html" 
    # , value=name
    )

@app.route('/welcome', methods=['POST'])
def welcome():
    return render_template("welcome.html", name=request.form['myName'])
