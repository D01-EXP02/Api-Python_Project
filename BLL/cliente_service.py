from BLL.connection_db import ConnectionManager
from DAL.cliente_repositorio import Cliente_repositorio


class Cliente_service():
    __connection_manager = ConnectionManager()
    __Cliente_servicio = Cliente_repositorio(__connection_manager.set_connection())

    def guardar_cliente(self, datos_cliente):
        self.__connection_manager.open_connection()
        self.__Cliente_servicio.guardar_cliente(datos_cliente)
        self.__connection_manager.close_connection()
        return "Se resgistro Correctamente!"

    def consultar_cliente(self):
        self.__connection_manager.open_connection()
        datos_cliente = self.__Cliente_servicio.All_clientes()
        self.__connection_manager.close_connection()
        return datos_cliente

    def filtrar_cliente_producto(self):
        return ""