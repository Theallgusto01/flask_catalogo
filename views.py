from app import app
from flask import render_template, url_for, request, redirect
from app import db, Filmes

@app.route('/')
def index():
    query = db.select(Filmes)
    filmes = db.session.execute(query).scalars().all()
    return render_template('index.html', title='Home', filmes=filmes)

@app.route('/addFilme')
def novo_filme():
    return render_template("cadastro.html", title="Adicionar Filme")

@app.route('/criar', methods=['POST'])
def criar():
    if request.method == 'POST':
        filme = Filmes(
            titulo=request.form['titulo'],
            genero=request.form['genero'],
            ano=request.form['ano']
        )
        db.session.add(filme)
        db.session.commit()
    return redirect(url_for('index'))