from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

def get_db_connection():
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(base_dir, 'database')
    os.makedirs(db_dir, exist_ok=True) 

    db_path = os.path.join(db_dir, 'usuarios.db')

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    conn = get_db_connection()
    usuario = conn.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()
    conn.close()

    if usuario and usuario['senha'] == senha:
        flash(f"Bem-vindo, {usuario['nome']}!", "success")
    else:
        flash("Login inválido. Verifique suas credenciais.", "danger")

    return redirect(url_for('index'))

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    conn = get_db_connection()
    usuario_existente = conn.execute('SELECT * FROM usuarios WHERE email = ?', (email,)).fetchone()

    if usuario_existente:
        flash("Usuário já cadastrado!", "warning")
    else:
        conn.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
        conn.commit()
        flash("Cadastro realizado com sucesso!", "success")

    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    criar_tabela()  
    app.run(debug=True)
