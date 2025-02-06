from src.database.db_sqlite import guardar, actualizar, eliminar
from src.models.tarea import Tarea

class TareaService:
    
    @staticmethod
    def traer_por_id(id: int):
        return Tarea.query.get_or_404(id)
    
    @staticmethod
    def agregar_tarea(tarea: Tarea):
        guardar(tarea)
    
    @staticmethod
    def actualizar_tarea(tarea: Tarea):
        t: Tarea = Tarea.query.get(tarea.id)
        
        if t:
            actualizar(tarea)
        else:
            raise ValueError(f'No existe la tarea con id {tarea.id}')

    @staticmethod
    def eliminar_tarea(id: int):
        t: Tarea = Tarea.query.get(id)
        
        if t:
            eliminar(t)
        else:
            raise ValueError(f'No existe la tarea con id {id}')