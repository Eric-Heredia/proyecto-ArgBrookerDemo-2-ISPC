class Cotizacion:
    def __init__(self, simbolo, nombre_empresa, ultimo_operado, cantidad_compra_diaria, precio_compra, precio_venta, apertura, minimo_diario, maximo_diario, ultimo_cierre):
        self.simbolo = simbolo
        self.nombre_empresa = nombre_empresa
        self.ultimo_operado = ultimo_operado
        self.cantidad_compra_diaria = cantidad_compra_diaria
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.apertura = apertura
        self.minimo_diario = minimo_diario
        self.maximo_diario = maximo_diario
        self.ultimo_cierre = ultimo_cierre

    def __repr__(self):
        return f"Cotizacion({self.simbolo}, {self.nombre_empresa}, Precio compra: ${self.precio_compra:.2f}, Precio venta: ${self.precio_venta:.2f})"
