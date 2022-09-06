import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/Hello/')
@app.route('/Hello/<name>')
def hello(name=None):
    return render_template('Hello.html', name=name)

@app.route('/')
def main():
    return render_template('calc.html')

@app.route('/calculaform', methods = ['POST', 'GET'])
def calculadora():
    
    valor1 = request.form['a']
    valor2 = request.form['b']
    op = request.form['op']
    
    a = int(valor1)
    b = int(valor2)

    if(op == 'soma'):
        result = a + b
    elif(op == 'subtracao'):
        result = a - b
    elif(op == 'divisao'):
        result = a / b
    elif(op == 'multiplicacao'):
        result = a * b 

    return str(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='127.0.0.1', port=port)