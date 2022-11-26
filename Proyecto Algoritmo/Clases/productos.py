class Producto:
    lista_productos = []
    def __init__(self, nombre, precio, tipo, adicional):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        self.adicional = adicional

    def encontrar_producto(nombre):
        for prod in Producto.lista_productos:
            if prod.nombre == nombre:
                return False