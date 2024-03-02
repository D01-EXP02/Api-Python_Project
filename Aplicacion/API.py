from fastapi import APIRouter
from Entity.cliente import Cliente
from Entity.producto import Producto
from BLL.cliente_service import Cliente_service
from BLL.producto_service import Producto_service
from BLL.connection_db import ConnectionManager

clientes = Cliente_service()
productos = Producto_service()
routes = APIRouter()
connection = ConnectionManager()

@routes.post("/Guardar_cliente")
def All_cliente(datos: Cliente):
    return clientes.guardar_cliente(datos)

@routes.get("/Consultar_ALL_clientes")
def All_cliente():
    return clientes.consultar_cliente()

@routes.get("/Consultar_clientes_por_Producto")
def Cliente_producto():
    return clientes.filtrar_cliente_producto()

@routes.post("/Registrar_Productos")
def guardar_producto(informacion: Producto, id: int):
    return productos.registrar_producto(informacion, id)