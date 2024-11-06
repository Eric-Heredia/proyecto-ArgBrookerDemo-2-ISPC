from dao.interface import UsuarioDAOInterface
from model.usuario import Usuario

class UsuarioDAO(UsuarioDAOInterface):
    def __init__(self, db_connection):
        self.db = db_connection

    def crear_usuario(self, usuario):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO usuarios (nombre, apellido, cuil, email, contraseña, saldo) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (usuario.nombre, usuario.apellido, usuario.cuil, usuario.email, usuario.contraseña, usuario.saldo))
        connection.commit()
        cursor.close()

    def obtener_usuario_por_id(self, id_usuario):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM usuarios WHERE id = %s"
        cursor.execute(query, (id_usuario,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def autenticar(self, email, contraseña):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM usuarios WHERE email = %s AND contraseña = %s"
        cursor.execute(query, (email, contraseña))
        result = cursor.fetchone()
        cursor.close()
        return result is not None

    def actualizar_usuario(self, usuario):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "UPDATE usuarios SET nombre=%s, apellido=%s, cuil=%s, email=%s, saldo=%s WHERE id=%s"
        cursor.execute(query, (usuario.nombre, usuario.apellido, usuario.cuil, usuario.email, usuario.saldo, usuario.id))
        connection.commit()
        cursor.close()

    def eliminar_usuario(self, id_usuario):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (id_usuario,))
        connection.commit()
        cursor.close()
