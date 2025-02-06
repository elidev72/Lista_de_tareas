from marshmallow import Schema, fields

class TareaSchema(Schema):
    id = fields.Int(dump_only=True)  # Solo se incluye al serializar
    titulo = fields.Str(required=True)
    descripcion = fields.Str(allow_none=True)  # Puede ser None
    completada = fields.Bool(missing=False)  # Valor por defecto es False si no se proporciona
