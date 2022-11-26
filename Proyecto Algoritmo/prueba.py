from Clases.equipo import Equipo
from Clases.estadio import Estadio
from Clases.partido import Partido
from Clases.cliente import Cliente
from Clases.compra import Compra
import requests
import json


def map_estadios(fila, columna):
    table = [["None"] * columna for _ in range(fila)]
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(fila):
        for j in range(columna):
            table[i][j] = (abc[j] + str(i+1))
    return table

def equipos():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
    else:
        print("Error")
    datos = json.loads(content.decode())
    for info in datos:
        Equipo.lista_equipos.append(Equipo(info['name'], info['fifa_code'], info['group'], int(info['id'])))
    return

def estadios():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
    else:
        print("Error")
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
    else:
        print("Error")
    datos = json.loads(content.decode())
    for info in datos:
        local = Equipo.buscar_pais(info['home_team']).pais
        visitante = Equipo.buscar_pais(info['away_team']).pais
        estadio = Estadio.buscar_id(info['stadium_id']).id
        fecha = info['date'].split()
        Partido.lista_partidos.append(Partido(local, visitante, fecha[0], fecha[1], estadio, int(info['id'])))
    return

def clientes():
    with open("Proyecto Algoritmo/Data/attempt.json", "r") as doc:
        datos = json.load(doc)
    for client in datos['clientes']:
        list_comp = []
        for purchase in client["compras"]:
            Compra.lista_compras.append(Compra(purchase["id del partido"], purchase["asiento"], purchase["tipo_entrada"], purchase["id de la compra"]))
            list_comp.append(purchase["id de la compra"])
        Cliente.lista_clientes.append(Cliente(client["nombre"], client["cedula"], client["edad"], list_comp))
    return

def realizar_compra():
    print("*******BIENVENIDO********")
    cedula = int(input("Ingrese su cedula: "))
    try:
        cliente = Cliente.buscar_cedula(cedula)
        error = cliente.nombre
    except AttributeError:
        nombre = input("Ingrese su nombre completo: ")
        edad = int(input("Ingrese su edad: "))
        Cliente.lista_clientes.append(Cliente(nombre, cedula, edad, []))
    finally:
        cliente = Cliente.buscar_cedula(cedula)
        print(f"Bienvenido {cliente.nombre}")     
    confirmar = "S"
    while confirmar == "S":
        id_match = int(input("Ingrese el ID del partido que le interesa: "))
        partido_object = Partido.buscar_id(id_match)
        estadio_object = partido_object.estadio
        cant_ticket = int(input("Ingrese cuantos tickets desea:"))
        print("Indique el tipo de entrada que desea, aplicara para todas las entradas de su compra actual")
        tipo_ticket = input("General o VIP?: ").upper()
        estadio_object.mostrar_mapa(partido_object)
        asientos = []
        while len(asientos) < cant_ticket:
            asientos.append(input("Ingrese el asiento que desea: "))
        if tipo_ticket == "VIP":
            monto = 120
        else:
            monto = 50
        recibo = {"Asiento": asientos, "Monto a pagar": monto*cant_ticket , "Partido": partido_object.titulo()}
        for key, data in recibo.items():
            print(key, '-----', data)
        proceed = input("Desea proceder?: ").upper()
        if proceed == "S":
            cliente.lista_compras.append(Compra(partido_object, asientos, tipo_ticket))
        confirmar = input("Desea realizar otra compra? (S/N)").upper()
    return

def busqueda():
    print("Escoja \n1.-Para buscar los partidos de un equipo especifico \n2.-Partidos en un estadio \n3.-Partidos en una fecha especifica \n4.-Ver todo \n5.-Salir")
    buscar = int(input("Ingrese el filtro por el que desea buscar:"))
    if buscar == 1:
        for team in Equipo.lista_equipos:
            team.mostrar_equipos()
        while True:
            code = input("Ingrese el codigo del equipo que le interesa:").upper()
            equipo_objeto = Equipo.buscar_codigo(code)
            if equipo_objeto == None:
                print("Equipo no encontrado, revise el codigo ingresado.")
                continue
            else:
                for match in Partido.lista_partidos:
                    if match.local == equipo_objeto.pais or match.visitante == equipo_objeto.pais:
                        match.mostrar()
            return
    elif buscar == 2:
        Estadio.info_estadios()
        estad = int(input("Ingrese el id del estadio que le interesa:"))
        for match in Partido.lista_partidos:
            if match.estadio == estad:
                match.mostrar()
    elif buscar == 3:
        fecha = input("Ingrese la fecha que le interesa (MM/D/YYYY):")
        for match in Partido.lista_partidos:
            if match.fecha == fecha:
                match.mostrar()
    elif buscar == 4:
        Partido.mostrar_compra()
    elif buscar == 5:
        return
    else:
        print("Error, intente de nuevo")

def restaurantes():
    for stad in Estadio.lista_estadios:
        print(stad.nombre)
        for item in stad.restaurante:
            for key,value in item.items():
                if type(value) == str:
                    print(key, "----", value)
                else:
                    for product in value:
                        for name, info in product.items():
                            print("     ",name, "----", info)
                        print("\n")
        print("\n")
    return

def guardar_json():
    lis_json = []
    for client in Cliente.lista_clientes:
        lis_comp = []
        for id in client.lista_compras:
            compra = Compra.find_compra(id)
            dicti = {"id del partido": compra.partido, "asiento": compra.asiento,"tipo_entrada": compra.tipo_entrada, "id de la compra": compra.id_compra}
            lis_comp.append(dicti)
        lis_json.append({"nombre": client.nombre, "cedula": client.cedula, "edad": client.edad, "compras": lis_comp})

    lis_restaurante = []
    for stad in Estadio.lista_estadios:
        lis_restaurante.append(stad.restaurante)

    data = {"clientes": lis_json, "restaurantes": lis_restaurante}

    with open("Proyecto Algoritmo/attempt.json", "w") as doc:
        json.dump(data, doc, indent=1)
    return

equipos()
estadios()
partidos()
clientes()

try:
    with open("prueba.json", "r") as doc:
        datos = json.load(doc)
except FileNotFoundError:
    print("Error")

# estadio = Estadio.lista_estadios[7]
# partido = Partido.buscar_id(31)
# ocupados = Compra.find_asientos_ocupados(partido)
# estadio.mostrar_mapa(partido, ocupados)

# mapa = estadio.mapa

# asiento = "W10"

# confir = False
# for fila in mapa:
#     if asiento in fila:
#         confir = True

# print(confir)
    

