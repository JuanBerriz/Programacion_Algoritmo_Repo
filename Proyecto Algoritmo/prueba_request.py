from equipo import Equipo
from estadio import Estadio
from partido import Partido
import json
import requests
import numpy as np

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
        Estadio.lista_estadios.append(Estadio(int(info['id']), info['name'], info['location'], info['capacity'], info['restaurants']))
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

def main():
    equipos()
    estadios()
    partidos()

        


main()