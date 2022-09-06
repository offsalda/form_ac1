import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    primos = "Tudo vai dar certo, caros alunos, confiem!"
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='127.0.0.1', port=port)