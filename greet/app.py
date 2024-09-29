from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    """ Display the Start Screen """
    return "<h1>This is the Start Page</h1>"

@app.route('/welcome')
def get_welcome():
    """ Display the Welcome Screen """
    return "<h1>welcome</h1>"

@app.route('/welcome/home')
def get_welcome_home():
    """ Display the Welcome Home Screen """
    return "<h1>welcome home</h1>"

@app.route('/welcome/back')
def get_welcome_back():
    """ Display the Welcome Back Screen """
    return "<h1>welcome back</h1>"