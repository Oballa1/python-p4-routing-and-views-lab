#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:num>')
def count(num):
    count = f''
    for n in range(num):
        count += f'{n}\n'
    return count
        
    
    


@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return "Invalid input. Please provide numbers."
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation. Please use +, -, *, or div."

    return str(result)
