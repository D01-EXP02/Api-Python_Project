from BLL.connection_db import ConnectionManager
from DAL.producto_repositorio import Producto_repositorio


class Producto_service():
    __connection_manager = ConnectionManager()
    __producto_servicio = Producto_repositorio(__connection_manager.set_connection())
    def registrar_producto(self, datos_producto):
        self.__connection_manager.open_connection()
        self.registrar_producto(datos_producto)
        self.__connection_manager.close_connection()
        return "Se registro Correctamente el producto!"