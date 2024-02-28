from BLL.connection_db import ConnectionManager
from DAL.cliente_repositorio import Cliente_repositorio


class Cliente_service():
    __connection_manager = ConnectionManager()
    __Cliente_servicio = Cliente_repositorio(__connection_manager.set_connection())

    def guardar_cliente(self, datoscliente):
        self.__connection_manager.open_connection()
        self.__Cliente_servicio.guardar_cliente(datoscliente)
        self.__connection_manager.close_connection()
        return "Se resgistro Correctamente!"

    def consultar_cliente(self):
        self.__connection_manager.open_connection()
        dato_cliente = self.__Cliente_servicio.All_clientes()
        self.__connection_manager.close_connection()
        return dato_cliente

    def filtrar_cliente_producto(self, info_cliente):
        self.__connection_manager.open_connection()
        lista_cliente = self.__Cliente_servicio.filtro_datos()

        for item in lista_cliente:
            if item.identificacion == info_cliente:
                cliente_encontrado = item
                return cliente_encontrado

        return lista_cliente