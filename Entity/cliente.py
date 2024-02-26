from pydantic import BaseModel
from datetime import date

class Cliente(BaseModel):
        nombre: str
        apellido: str
        identificacion: str
        fecha_nacimiento: date
        sexo: str


class Cliente_respuesta(BaseModel):
        nombre: str = None
        apellido: str = None
        identificacion: str = None
        fecha_nacimiento: date = None
        sexo: str = None
