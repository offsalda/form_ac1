import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

#PUXA O FORMULARIO HTML "EXEMPLO"
@app.route('/teste2')
def index2():
    return render_template('exemplo.html')


#PUXAR PARAMETRO DO AJAX
@app.route('/api/exemplo', methods=['POST'])
def exemplo():
    json = request.get_json()
    nome2 = json['nome']
    categ2 = json['categ']
    print(nome2)
    print(categ2)
    return jsonify(categ=categ2)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)