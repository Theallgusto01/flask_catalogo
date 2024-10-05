from sqlalchemy import create_engine, select, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, sessionmaker
import pymysql.cursors


class Base(DeclarativeBase):
    pass

class Filmes(Base):
    __tablename__ = 'Filmes'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column()
    genero: Mapped[str] = mapped_column()
    ano: Mapped[int] = mapped_column()


engine = create_engine("mysql+pymysql://root:1234@localhost:3306/MY_DATABASE")
Session = sessionmaker(engine)

def add_filme(novo_filme):
    with Session() as session:
        session.begin()
        try:
            session.add(novo_filme)
        except:
            session.rollback()
            raise
        else:
            session.commit()

def list_filmes():
    with Session() as session:
        resp = select(Filmes)
        rows = session.execute(resp).scalars().all()
    return rows
