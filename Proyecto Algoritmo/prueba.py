import numpy as np
from estadio import Estadio
from partido import Partido
from equipo import Equipo
from partido import Partido
from compra import Compra
from cliente import Cliente
import requests
import json
from tabulate import tabulate

def clientes():
    with open(r"C:\Users\juanb\Desktop\Unimet\Programacion_Algoritmo_Repo\Proyecto Algoritmo\clients.json", "r") as doc:
        datos = json.load(doc)
    for client in datos:
        list_comp = []
        for purchase in client["compras"]:
            partido_object = Partido.buscar_id(purchase["id del partido"])
            list_comp.append(Compra(partido_object, purchase["asiento"], purchase["tipo_entrada"]))
        Compra.add_main_list(list_comp)
        Cliente.lista_clientes.append(Cliente(client["nombre"], client["cedula"], client["edad"], list_comp))
    return



def map_estadios(fila, columna):
    d = [[[] for c in range(fila)]]
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    indice = 0
    for num in range(fila):
        for let in abc[0:columna]:
            fil = d[0]
            fil[indice].append(let + str(num+1))
            if len(fil[indice]) == columna:
                indice += 1
    return d

def equipos():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
    datos = json.loads(content.decode())
    for info in datos:
        Equipo.lista_equipos.append(Equipo(info['name'], info['fifa_code'], info['group'], int(info['id'])))
    return

def estadios():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
    datos = json.loads(content.decode())
    for info in datos:
        mapa = map_estadios(info['capacity'][0], info['capacity'][1])
        Estadio.lista_estadios.append(Estadio(int(info['id']), info['name'], info['location'], info['capacity'], info['restaurants'], mapa))
    return

def partidos():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
    datos = json.loads(content.decode())
    for info in datos:
        local = Equipo.buscar_pais(info['home_team'])
        visitante = Equipo.buscar_pais(info['away_team'])
        estadio = Estadio.buscar_id(info['stadium_id'])
        fecha = info['date'].split()
        Partido.lista_partidos.append(Partido(local, visitante, fecha[0], fecha[1], estadio, int(info['id'])))
    return

clientes()
equipos()
estadios()
partidos()

Estadio.lista_estadios[0].mostrar_mapa(Partido.lista_partidos[33])
mapa = Estadio.lista_estadios[0].mapa
print(Estadio.lista_estadios[0].nombre)
for info in mapa:
    print(tabulate(info, tablefmt="grid"))





