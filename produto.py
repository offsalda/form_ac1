import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('produto.html')

@app.route('/produto', methods=['POST','GET'])
def gravar():
  nome = request.form['nome']
  preco = request.form['preco']
  categoria = request.form['categoria']
  if nome and preco and categoria:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_product (product_name, product_preco, product_categoria) VALUES (%s, %s, %s)', (nome, preco, categoria))
    conn.commit()
  return render_template('produto.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select product_name, product_preco, product_categoria from tbl_product')
  data = cursor.fetchall()
  conn.commit()
  return render_template('listar.html', datas=data)

if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 5004))
    app.run(host='0.0.0.0', port=port)
