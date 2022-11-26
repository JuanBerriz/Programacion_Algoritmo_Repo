from Clases.equipo import Equipo
from Clases.estadio import Estadio
from Clases.partido import Partido
from Clases.cliente import Cliente
from Clases.compra import Compra
import json
import requests

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

def partidos():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
    datos = json.loads(content.decode())
    for info in datos:
        local = info['home_team']
        visitante = info['away_team']
        estadio = info['stadium_id']
        fecha = info['date'].split()
        Partido.lista_partidos.append(Partido(local, visitante, fecha[0], fecha[1], estadio, int(info['id'])))
    return

def clientes():
    try:
        with open("Proyecto Algoritmo\Data\clients.json", "r") as doc:
            datos = json.load(doc)
        for client in datos:
            list_comp = []
            for purchase in client["compras"]:
                Compra.lista_compras.append(Compra(purchase["id del partido"], purchase["asiento"], purchase["tipo_entrada"], purchase["id de la compra"]))
                list_comp.append(purchase["id de la compra"])
            Cliente.lista_clientes.append(Cliente(client["nombre"], client["cedula"], client["edad"], list_comp))
    except FileNotFoundError:
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
        busqueda()
        id_match = int(input("Ingrese el ID del partido que le interesa: "))
        partido_object = Partido.buscar_id(id_match)
        estadio_object = Estadio.buscar_id(partido_object.estadio)
        tipo_ticket = input("Cual entrada desea? (General/VIP): ").upper()
        ocupados = Compra.find_asientos_ocupados(partido_object)
        estadio_object.mostrar_mapa(partido_object, ocupados)
        asiento = input("Ingrese el asiento que desea: ").upper()
        if tipo_ticket == "VIP":
            monto = 120
        else:
            monto = 50
        iden = len(Compra.lista_compras) + 1
        recibo = {"Partido": partido_object.titulo(), "Asiento": asiento, "Entrada": tipo_ticket, "Monto a pagar": monto, "ID de la compra": iden}
        for key, data in recibo.items():
            print(key, '-----', data)
        proceed = input("Desea proceder?: ").upper()
        if proceed == "S":
            Compra.lista_compras.append(partido_object.id, asiento, tipo_ticket, iden)
            cliente.lista_compras.append(iden)
            print("Su compra ha sido registrada exitosamente. Por favor recordarse del id de su compra.")
        confirmar = input("Desea realizar otra compra? (S/N)").upper()
    return

def compra_alimentos():
    cedula = int(input("Ingrese su cedula: "))
    cliente = Cliente.buscar_cedula(cedula)
    cliente.mostrar_compras()
    print()
    espec = int(input("Ingrese el ID de la compra que corresponde al partido: "))
    buy = Compra.find_compra(espec)
    if buy.tipo_entrada != "VIP":
        print("No aplica para comprar alimentos.")
    else:
        return

def main():
    equipos()
    estadios()
    partidos()
    clientes()
    while True:
        print("Ingrese la accion que desea realizar \n1.-Buscar informacion de los partidos \n2.-Comprar una entrada \n4.-Salir")
        accion = int(input("Accion: "))
        if accion == 1:
            busqueda()
        elif accion == 2:
            realizar_compra()
        elif accion == 4:
            lis_json = []
            for client in Cliente.lista_clientes:
                lis_comp = []
                for id in client.lista_compras:
                    compra = Compra.find_compra(id)
                    dicti = {"id del partido": compra.partido, "asiento": compra.asiento,"tipo_entrada": compra.tipo_entrada, "id de la compra": compra.id_compra}
                    lis_comp.append(dicti)
                lis_json.append({"nombre": client.nombre, "cedula": client.cedula, "edad": client.edad, "compras": lis_comp})
            with open("Proyecto Algoritmo\Data\clients.json", "w") as doc:
                json.dump(lis_json, doc, indent=1)
            break
    return

main()
