from Entity.cliente import Cliente, Cliente_respuesta
from Entity.producto import Producto_respuesta

class Cliente_repositorio():
    def __init__(self, connection):
        self.connetion = connection

    def todos_cliente(self):
        return self.__Clientes

    def All_clientes(self):
        lista_sql = []
        cursor = self.connetion.cursor()
        cursor.execute(
                "SELECT Nombre, Apellido, Identificacion, Sexo, Fecha_Nacimiento  "
                "FROM clientes e "
                "LEFT JOIN producto n "
                "ON e.ID = n.Id_cliente "
        )

        datos_cliente = cursor.fetchall()
        for item in datos_cliente:
            lista_sql.append(self.mapear(item))

        return lista_sql

    def filtro_datos(self):
        lista_sql = []
        cursor = self.connetion.cursor()
        cursor.execute(
            "SELECT Nombre, Apellido, Identificacion, Sexo, Fecha_Nacimiento, Valor, Nombre_Producto "
            "FROM clientes e "
            "JOIN producto n "
            "ON e.ID = n.Id_cliente "
        )

        datos_cliente = cursor.fetchall()
        for item in datos_cliente:
            lista_sql.append(self.mapear(item))

        return lista_sql

    def guardar_cliente(self, cliente: Cliente):
        cursor = self.connetion.cursor()
        sql = ("INSERT INTO clientes(Nombre, Apellido, Identificacion, Sexo, Fecha_Nacimiento) "
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

    def mapear(self, registro):
        nombre, apellido, identificacion, sexo, fecha_nacimiento, valor_producto, nombre_producto = registro
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