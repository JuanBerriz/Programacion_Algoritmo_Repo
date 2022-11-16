from termcolor import colored
from compra import Compra
from partido import Partido

class Estadio:
    lista_estadios = []
    def __init__(self, id, nombre, ubicacion, capacidad, restaurante, mapa):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.restaurante = restaurante
        self.mapa = mapa

    def buscar_id(id):
        for stadium in Estadio.lista_estadios:
            if stadium.id == id:
                return stadium

    def info_restaurantes(self):
        for info in Estadio.lista_estadios[0].restaurante:
            for key, value in info.items():
                if type(value) == list:
                    for name in value:
                        for tipo, data in name.items():
                            print(tipo, '---', data)
                else:
                    print(key, '---', value)

    def prueba(self):
        print(type(self.id))
        print(type(self.nombre))
        print(type(self.ubicacion))
        print(type(self.capacidad))
        print(type(self.restaurante))
        print(type(self.mapa))
 
    def mostrar_mapa(self, partido):
        def cambiar_color(asiento, game):
            ocupados = Compra.find_asientos_ocupados(game)
            for ocup in ocupados:
                if asiento == ocup:
                    out = colored(asiento, "white", "on_red")
                    return out
            else:
                return asiento
        print(f"Nombre del estadio: {self.nombre}")
        print(f"Partido Interesado: {partido.titulo()}")
        fila = self.capacidad[0]
        columna = self.capacidad[1]
        for item in self.mapa:
            for i in range(fila):
                for j in range(columna):
                    att = cambiar_color(item[i][j], partido)
                    if i < 9 and j != columna-1:
                        print(att, end="-----")
                    elif j == columna-1:
                        print(att, end="")
                    else:
                        print(att, end="----")
                print("\n")
            print("\n")
