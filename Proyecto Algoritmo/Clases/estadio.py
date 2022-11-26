from termcolor import colored
from tabulate import tabulate

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

    def buscar_nombre(nombre):
        for stadium in Estadio.lista_estadios:
            if stadium.nombre == nombre:
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
 
    def mostrar_mapa(self, partido, ocupados):
        def cambiar_color(asiento):
            #camb = colored(asiento, "red")
            camb = colored(asiento, "white", "on_red")
            return camb
        print(f"Nombre del estadio: {self.nombre}")
        print(f"Partido Interesado: {partido.titulo()}")
        fila = self.capacidad[0]
        columna = self.capacidad[1]
        table = self.mapa
        for i in range(fila):
            for j in range(columna):
                for ocup in ocupados:
                    if ocup == table[i][j]:
                        table[i][j] = cambiar_color(table[i][j])

        print(tabulate(table, tablefmt="grid"))

    def info_estadios():
        for stadium in Estadio.lista_estadios:
            print(f"Nombre: {stadium.nombre}")
            print(f"Id del Estadio: {stadium.id}\n")
