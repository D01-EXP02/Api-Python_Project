from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from Entity.producto import Producto, producto_respuesta
from BLL.connection_db import ConnectionManager


class Producto_repositorio():
    def __init__(self, connection):
         self.connection = connection

    def guardar_cliente(self, producto: Producto):
        cursor = self.connection.cursor()
        sql = ("INSERT INTO producto(Nombre_producto,Valor) "
               "values(%s,%s) ")

        values = (
            producto.nombre,
            producto.valor
        )

        cursor.execute(sql, values)
        self.connection.commit()
        cursor.close()