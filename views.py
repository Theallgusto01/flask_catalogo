from app import app
from flask import render_template, url_for, request, redirect
from app import db
from models import Filmes


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
        exist = db.session.execute(select(Filmes)).scalars.all()
        if request.form['titulo'] in exist:
            
        db.session.add(filme)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/filme/<int:id>')
def view(id):
    filme = db.session.execute(db.select(Filmes).filter_by(id=id)).scalars().first()
    return render_template('edit.html', filme=filme)


@app.route('/edit/<int:id>', methods=["POST"])
def update(id):

    filme = db.session.execute(db.select(Filmes).filter_by(id=id)).scalars().first()
    filme.titulo = request.form['titulo']
    filme.ano = request.form['ano']
    filme.genero = request.form['genero']
    filme.verified = True   
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    filme = db.session.execute(db.select(Filmes).filter_by(id=id)).scalars().first()
    db.session.delete(filme)
    db.session.commit()
    return redirect(url_for('index'))