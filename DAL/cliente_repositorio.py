from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from Entity.cliente import Cliente, Cliente_respuesta
from BLL.connection_db import ConnectionManager

class Cliente_repositorio():
    def __init__(self, connection):
        self.connetion = connection

    def todos_cliente(self):
        return self.__Clientes

    def All_clientes(self):
        clientes = []
        cursor = self.connetion.cursor()
        cursor.execute(
                "SELECT Nombre, Apellido, Identificacion, Sexo, fecha_nacimiento  "
                "FROM clientes e "
                "LEFT JOIN producto n "
                "ON e.id = n.Id_cliente "
                "GROUP BY identificacion "
        )

        datos_cliente = cursor.fetchall()
        for item in datos_cliente:
            clientes.append(self.mapeado(item))

    def guardar_cliente(self, cliente: Cliente):
        cursor = self.connetion.cursor()
        sql = ("INSERT INTO clientes(Nombre, Apellido, Identificacion, Sexo, fecha_nacimiento) "
             "values(%s,%s,%s,%s,%s) ")

        values = (
            cliente.nombre,
            cliente.apellido,
            cliente.identificacion,
            cliente.sexo,
            str(cliente.fecha_nacimiento)
        )

        cursor.execute(sql,values)
        self.connetion.commit()
        cursor.close()

    def mapeado(self, registro):
        return Cliente_respuesta(
            nombre=registro[0],
            Apellido=registro[1],
            identificacion=registro[2],
            sexo=registro[3],
            fechaNacimiento=registro[4]
        )

