from pydantic import BaseModel

class Producto(BaseModel):
        nombre_producto: str
        valor: int

class Producto_respuesta(BaseModel):
        nombre_producto: str = None
        valor: int
