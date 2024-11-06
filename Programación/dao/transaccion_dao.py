from dao.interface import TransaccionDAOInterface
from model.transaccion import Transaccion

class TransaccionDAO(TransaccionDAOInterface):
    def __init__(self, db_connection):
        self.db = db_connection

    def registrar_transaccion(self, transaccion):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO transacciones (usuario_id, accion_id, cantidad, tipo, precio, fecha, comision) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (transaccion.usuario_id, transaccion.accion_id, transaccion.cantidad, transaccion.tipo, transaccion.precio, transaccion.fecha, transaccion.comision))
        connection.commit()
        cursor.close()

    def obtener_transacciones_por_usuario(self, id_usuario):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM transacciones WHERE usuario_id = %s"
        cursor.execute(query, (id_usuario,))
        result = cursor.fetchall()
        cursor.close()
        return result

    def obtener_transaccion_por_id(self, id_transaccion):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM transacciones WHERE id = %s"
        cursor.execute(query, (id_transaccion,))
        result = cursor.fetchone()
        cursor.close()
        return result
