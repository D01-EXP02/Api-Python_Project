from BLL.connection_db import ConnectionManager
from BLL.cliente_service import Cliente_service
from DAL.producto_repositorio import Producto_repositorio


class Producto_service():
    __connection_manager = ConnectionManager()
    __cliente = Cliente_service()
    __producto_servicio = Producto_repositorio(__connection_manager.set_connection())
    def registrar_producto(self, datos_producto , id):
        self.__connection_manager.open_connection()

        self.__producto_servicio.guardar_producto(datos_producto, id)
        self.__connection_manager.close_connection()
        return "Se registro Correctamente el producto!"