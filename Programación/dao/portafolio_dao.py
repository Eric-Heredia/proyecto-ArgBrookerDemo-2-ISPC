from dao.interface import PortafolioDAOInterface
from model.portafolio import Portafolio

class PortafolioDAO(PortafolioDAOInterface):
    def __init__(self, db_connection):
        self.db = db_connection

    def obtener_portafolio_por_usuario(self, id_usuario):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM portafolios WHERE usuario_id = %s"
        cursor.execute(query, (id_usuario,))
        result = cursor.fetchall()
        cursor.close()
        return result

    def actualizar_portafolio(self, portafolio):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "UPDATE portafolios SET acciones=%s, valor_comprometido=%s WHERE usuario_id=%s"
        cursor.execute(query, (portafolio.acciones, portafolio.valor_comprometido, portafolio.usuario_id))
        connection.commit()
        cursor.close()
