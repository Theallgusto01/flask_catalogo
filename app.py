from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


app = Flask(__name__)

class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@localhost:3306/DATABASE"

db = SQLAlchemy(model_class=Base)

db.init_app(app)

class Filmes(Base):
    __tablename__ = "Filmes"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)


from views import *

def main():
    app.run(debug=True, host='0.0.0.0', port=8000)

if __name__ ==  '__main__':
    main()