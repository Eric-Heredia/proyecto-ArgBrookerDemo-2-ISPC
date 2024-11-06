class Transaccion:
    def __init__(self, id_usuario, simbolo, cantidad, tipo, precio, fecha, comision):
        self.id_usuario = id_usuario
        self.simbolo = simbolo
        self.cantidad = cantidad
        self.tipo = tipo  # "Compra" o "Venta"
        self.precio = precio
        self.fecha = fecha
        self.comision = comision

    def __repr__(self):
        return f"Transaccion({self.id_usuario}, {self.simbolo}, {self.cantidad}, {self.tipo}, Precio: ${self.precio:.2f}, Comisión: ${self.comision:.2f})"
