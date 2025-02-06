from flask_sqlalchemy import SQLAlchemy

url_db: str = 'sqlite:///lista_de_tareas.db'

db = SQLAlchemy()
