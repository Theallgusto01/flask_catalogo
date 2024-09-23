from app import app
from flask import render_template, url_for
from testes_sqlalchemy import list_filmes

@app.route('/')
def index():
    filmes = list_filmes()

    return render_template('index.html', title='Home', filmes=filmes)

