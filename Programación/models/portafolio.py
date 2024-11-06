class Portafolio:
    def __init__(self, id_usuario, simbolo, cantidad, precio_compra):
        self.id_usuario = id_usuario
        self.simbolo = simbolo
        self.cantidad = cantidad
        self.precio_compra = precio_compra

    def __repr__(self):
        return f"Portafolio({self.id_usuario}, {self.simbolo}, {self.cantidad} acciones, Precio compra: ${self.precio_compra:.2f})"
