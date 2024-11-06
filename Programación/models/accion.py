class Accion:
    def __init__(self, simbolo, nombre_empresa, precio_actual):
        self.simbolo = simbolo
        self.nombre_empresa = nombre_empresa
        self.precio_actual = precio_actual

    def __repr__(self):
        return f"Accion({self.simbolo}, {self.nombre_empresa}, Precio actual: ${self.precio_actual:.2f})"
