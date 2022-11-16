class Compra:
    lista_compras = []
    def __init__(self, partido, asiento, tipo_entrada):
        self.partido = partido
        self.asiento = asiento
        #self.codigo = codigo
        self.tipo_entrada = tipo_entrada
    
    def mostrar(self):
        print(f"Partido: {(self.partido).titulo()}")
        print(f"Asiento: {self.asiento}")
        print(f"Entrada: {self.tipo_entrada}")
        print("\n")

    def find_asientos_ocupados(partido):
        taken = []
        for compra in Compra.lista_compras:
            if compra.partido == partido:
                taken.append(compra.asiento)
        return taken

    def add_main_list(list):
        for item in list:
            Compra.lista_compras.append(item)
        return

