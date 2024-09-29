# This app will be used to handle various calculations with a given 
#   opeator. 
from flask import Flask, request 
from operations import add,sub,mult,div

app = Flask(__name__)

@app.route('/')
def home():
    """ Display the Start Screen """
    return "<h1>This is the Start Page for Calc</h1>"

@app.route('/add')
def get_add():
    """ Add two values together and return the sum """
    # using the basic request here and will cast the value as an int later
    a = request.args["a"]
    b = request.args["b"]
    sum = add(int(a), int(b))

    return f'{sum}' 

@app.route('/sub')
def get_sub():
    """ Subtract the b value from the a and return the difference """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    diff = sub(a, b)

    return f'{diff}' 


@app.route('/mult')
def get_mult():
    """ Multiply two values together and return the product """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    product = mult(a, b)

    return f'{product}' 

@app.route('/div')
def get_division():
    """ Divide value a by value b return the quotient """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    quotient = div(a, b)

    return f'{quotient}' 

# Further Study Extension

# Example with a dictionary
operator = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route("/math/<calc>")
def get_math(calc):
    a = request.args['a']
    b = request.args['b']
    answer = operator[calc](int(a), int(b))

    return f'The answer is: {answer}'