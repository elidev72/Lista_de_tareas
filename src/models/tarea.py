from src.database.db_sqlite import db

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(250))
    completada = db.Column(db.Boolean, default=False)
