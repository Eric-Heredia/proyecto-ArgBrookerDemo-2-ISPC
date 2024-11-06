from dao.interface import AccionDAOInterface
from model.accion import Accion

class AccionDAO(AccionDAOInterface):
    def __init__(self, db_connection):
        self.db = db_connection

    def obtener_accion_por_simbolo(self, simbolo):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM acciones WHERE simbolo = %s"
        cursor.execute(query, (simbolo,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def actualizar_precio_accion(self, simbolo, nuevo_precio):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "UPDATE acciones SET precio_actual = %s WHERE simbolo = %s"
        cursor.execute(query, (nuevo_precio, simbolo))
        connection.commit()
        cursor.close()
