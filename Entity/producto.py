from pydantic import BaseModel

class Producto(BaseModel):
        nombre: str
        valor: str

class producto_respuesta(BaseModel):
        nombre: str = None
        valor: str = None