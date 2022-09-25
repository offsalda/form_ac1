import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__, template_folder="Templates")
#app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('produto.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  nome = request.form['nome']
  preco = request.form['preco']
  categoria = request.form['categoria']
  if nome and preco and categoria:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_produto (produto_nome, produto_preco, produto_categoria) VALUES (%s, %s, %s)', (nome, preco, categoria))
    conn.commit()
  return render_template('produto.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select produto_name, produto_preco, produto_endereco from tbl_produto')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 5004))
    app.run(host='0.0.0.0', port=port)
