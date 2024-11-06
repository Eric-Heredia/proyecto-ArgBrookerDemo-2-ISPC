class Usuario:
    def __init__(self, id_usuario=None, nombre="", apellido="", cuil="", email="", contraseña="", saldo=1000000.0):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.email = email
        self.contraseña = contraseña
        self.saldo = saldo

    def __repr__(self):
        return f"Usuario({self.id_usuario}, {self.nombre}, {self.apellido}, {self.cuil}, {self.email}, Saldo: ${self.saldo:.2f})"
