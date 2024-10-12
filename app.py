from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@localhost:3306/MY_DATABASE"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

from views import *

def main():
    app.run(debug=True, host='0.0.0.0', port=8000)

if __name__ ==  '__main__':
    with app.app_context():
        db.create_all()
    main()