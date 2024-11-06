from abc import ABC, abstractmethod

# Interface para UsuarioDAO
class UsuarioDAOInterface(ABC):
    @abstractmethod
    def crear_usuario(self, usuario):
        pass

    @abstractmethod
    def obtener_usuario_por_id(self, id_usuario):
        pass

    @abstractmethod
    def autenticar(self, email, contraseña):
        pass

    @abstractmethod
    def actualizar_usuario(self, usuario):
        pass

    @abstractmethod
    def eliminar_usuario(self, id_usuario):
        pass


# Interface para TransaccionDAO
class TransaccionDAOInterface(ABC):
    @abstractmethod
    def registrar_transaccion(self, transaccion):
        pass

    @abstractmethod
    def obtener_transacciones_por_usuario(self, id_usuario):
        pass

    @abstractmethod
    def obtener_transaccion_por_id(self, id_transaccion):
        pass


# Interface para PortafolioDAO
class PortafolioDAOInterface(ABC):
    @abstractmethod
    def obtener_portafolio_por_usuario(self, id_usuario):
        pass

    @abstractmethod
    def actualizar_portafolio(self, portafolio):
        pass


# Interface para CotizacionDAO
class CotizacionDAOInterface(ABC):
    @abstractmethod
    def obtener_cotizacion_por_simbolo(self, simbolo):
        pass

    @abstractmethod
    def listar_cotizaciones(self):
        pass


# Interface para AccionDAO
class AccionDAOInterface(ABC):
    @abstractmethod
    def obtener_accion_por_simbolo(self, simbolo):
        pass

    @abstractmethod
    def actualizar_precio_accion(self, simbolo, nuevo_precio):
        pass
