from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

url_db: str = 'sqlite:///lista_de_tareas.db'

db = SQLAlchemy()

def __manejar_excepcion(e: SQLAlchemyError):
    db.session.rollback()
    raise Exception("ERROR en la capa de acceso a datos") from e

def guardar(dato):
    try:
        db.session.add(dato)
        db.session.commit()
    except SQLAlchemyError as e:
        __manejar_excepcion(e)

def actualizar(dato):
    try:
        db.session.merge(dato)
        db.session.commit()
    except SQLAlchemyError as e:
        __manejar_excepcion(e)

def eliminar(dato):
    try:
        db.session.delete(dato)
        db.session.commit()
    except SQLAlchemyError as e:
        __manejar_excepcion(e)
