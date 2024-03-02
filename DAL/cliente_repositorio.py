from Entity.cliente import Cliente, Cliente_respuesta
from Entity.producto import Producto_respuesta
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

class Cliente_repositorio():
    def __init__(self, connection):
        self.connetion = connection

    def todos_cliente(self):
        return self.__Clientes

    def All_clientes(self):
        lista_sql = []
        cursor = self.connetion.cursor()
        cursor.execute(
                "SELECT Nombre, Apellido, Identificacion, Fecha_Nacimiento, Sexo  "
                "FROM clientes e "
                "LEFT JOIN producto n "
                "ON e.ID = n.Id_cliente "
        )

        datos_cliente = cursor.fetchall()
        for item in datos_cliente:
            lista_sql.append(self.mapear_cliente(item))
        return  lista_sql

    def filtro_datos(self):
        lista_sql_filtro = []
        cursor = self.connetion.cursor()
        cursor.execute(
            "SELECT Nombre, Apellido, Identificacion, Sexo, Fecha_Nacimiento, Valor, Nombre_Producto "
            "FROM clientes e "
            "JOIN producto n "
            "ON e.ID = n.Id_cliente "
        )

        datos_cliente = cursor.fetchall()
        for item in datos_cliente:
            lista_sql_filtro.append(self.mapear_filtro(item))

        return lista_sql_filtro

    def guardar_cliente(self, cliente: Cliente):
        cursor = self.connetion.cursor()
        sql = ("INSERT INTO clientes(Nombre, Apellido, Identificacion, Sexo, Fecha_Nacimiento) "
             "values(%s,%s,%s,%s,%s) ")

        values = (
            cliente.nombre,
            cliente.apellido,
            cliente.identificacion,
            cliente.sexo,
            cliente.fecha_nacimiento
        )

        cursor.execute(sql,values)
        self.connetion.commit()
        cursor.close()

    def mapear_filtro(self, registrofiltrar):
        nombre, apellido, identificacion, sexo, fecha_nacimiento, valor_producto, nombre_producto = registrofiltrar
        return Cliente_respuesta(
            nombre=nombre,
            apellido=apellido,
            identificacion=identificacion,
            sexo=sexo,
            fecha_nacimiento=fecha_nacimiento,
            producto_respuesta=Producto_respuesta(
                nombre_producto=str(nombre_producto),
                valor=int(valor_producto)
            )
        )

    def mapear_cliente(self, registro):
        nombre, apellido, identificacion, fecha_nacimiento, sexo = registro
        return Cliente_respuesta(
            nombre=nombre,
            apellido=apellido,
            identificacion=identificacion,
            fecha_nacimiento=fecha_nacimiento,
            sexo=sexo,
        )
