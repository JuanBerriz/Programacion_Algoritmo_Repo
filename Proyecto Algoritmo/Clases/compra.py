from Clases.partido import Partido

class Compra:
    lista_compras = []
    def __init__(self, partido_id, asiento, tipo_entrada, id):
        self.partido = partido_id
        self.asiento = asiento
        self.tipo_entrada = tipo_entrada
        self.id_compra = id
    
    def mostrar(self):
        print(f"Partido: {(Partido.buscar_id(self.partido)).titulo()}")
        print(f"Asiento: {self.asiento}")
        print(f"Tipo de entrada: {self.tipo_entrada}")
        print(f"Id de la compra: {self.id_compra}")
        print("\n")

    def find_asientos_ocupados(partido):
        taken = []
        for compra in Compra.lista_compras:
            if compra.partido == partido.id:
                taken.append(compra.asiento)
        return taken

    def find_compra(id):
        for compra in Compra.lista_compras:
            if compra.id_compra == id:
                return compra

    def info_compra(self):
        print(f"Partido: {(Partido.buscar_id(self.partido)).titulo()}")
        print(f"Id de la compra: {self.id_compra}")
        print("\n")
