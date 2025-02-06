from flask import request, abort
from src.app import app
from src.schemas.tarea_schema import TareaSchema
from src.services.tarea_service import TareaService as ts, Tarea

tsc = TareaSchema()

@app.route('/api/crear-tarea', methods=['POST'])
def crear_tarea():
    dato_json = request.get_json()
    
    try:
        dato_tarea = tsc.load(dato_json)
        tarea = Tarea(**dato_tarea)
        ts.agregar_tarea(tarea=tarea)
    except Exception as e:
        abort(400, e)
    
    return tsc.dump(tarea), 201

@app.route('/api/mostrar-tarea/<int:id>')
def mostrar_tarea(id):
    return tsc.dump(ts.traer_por_id(id)), 200

@app.route('/api/actualizar-tarea/<int:id>', methods=['PUT'])
def actualizar_tarea(id: int):
    dato_json = request.get_json()
    
    try:
        dato_tarea = tsc.load(dato_json)
        tarea: Tarea = Tarea(**dato_tarea)
        tarea.id = id
        ts.actualizar_tarea(tarea)
    except ValueError as ve:
        abort(404, ve)
    except Exception as e:
        abort(400, e)

    return tsc.dump(ts.traer_por_id(id)), 200

@app.route('/api/eliminar-tarea/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    try:
        ts.eliminar_tarea(id)
    except ValueError as ve:
        abort(404, ve)
    except Exception as e:
        abort(400, e)

    return '', 204