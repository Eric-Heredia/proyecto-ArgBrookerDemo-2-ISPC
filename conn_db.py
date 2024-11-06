import mysql.connector
from mysql.connector import Error
import configparser

class DatabaseConnection:
    def __init__(self, config_file="config.ini"):
        self.config_file = config_file
        self.connection = None

    def connect(self):
        # Leer configuración de archivo config.ini
        config = configparser.ConfigParser()
        config.read(self.config_file)

        try:
            # Crear la conexión a la base de datos usando la sección [database]
            self.connection = mysql.connector.connect(
                host=config['database']['host'],
                user=config['database']['user'],
                password=config['database']['password'],
                database=config['database']['database']
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos.")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.connection = None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada correctamente.")

    def get_connection(self):
        if not self.connection or not self.connection.is_connected():
            self.connect()
        return self.connection
