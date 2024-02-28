from Entity.producto import Producto


class Producto_repositorio():
    def __init__(self, connection):
         self.connection = connection

    def guardar_producto(self, producto: Producto, id: int):
        cursor = self.connection.cursor()
        sql = ("INSERT INTO producto(Id_cliente,Nombre_producto,Valor) "
               "values(%s,%s,%s) ")

        values = (
            id,
            producto.nombre_producto,
            producto.valor
        )

        cursor.execute(sql, values)
        self.connection.commit()
        cursor.close()
