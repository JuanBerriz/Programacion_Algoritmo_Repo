from Clases.compra import Compra

class Cliente:
    lista_clientes = []
    def __init__(self, nombre, cedula, edad, lista_compras):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.lista_compras = lista_compras

    def buscar_cedula(cedu):
        for client in Cliente.lista_clientes:
            if client.cedula == cedu:
                return client

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"cedula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Compras: {self.lista_compras}")
        print("\n")

    def mostrar_compras(self):
        for id in self.lista_compras:
            att = Compra.find_compra(id)
            att.info_compra()


