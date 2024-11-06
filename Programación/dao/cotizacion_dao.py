from dao.interface import CotizacionDAOInterface
from model.cotizacion import Cotizacion

class CotizacionDAO(CotizacionDAOInterface):
    def __init__(self, db_connection):
        self.db = db_connection

    def obtener_cotizacion_por_simbolo(self, simbolo):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM cotizaciones WHERE simbolo = %s"
        cursor.execute(query, (simbolo,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def listar_cotizaciones(self):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM cotizaciones"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
