from sqlalchemy.orm import mapped_column, Mapped
from app import db


class Filmes(db.Model):
    __tablename__ = "Filmes"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)