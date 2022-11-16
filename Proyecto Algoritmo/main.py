from equipo import Equipo
from estadio import Estadio
from partido import Partido
from cliente import Cliente
from compra import Compra
import json
import requests

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

def clientes():
    with open("Proyecto Algoritmo\clients.json", "r") as doc:
        datos = json.load(doc)
    for client in datos:
        list_comp = []
        for purchase in client["compras"]:
            partido_object = Partido.buscar_id(purchase["id del partido"])
            list_comp.append(Compra(partido_object, purchase["asiento"], purchase["tipo_entrada"]))
        Compra.add_main_list(list_comp)
        Cliente.lista_clientes.append(Cliente(client["nombre"], client["cedula"], client["edad"], list_comp))
    doc.close()
    return

def busqueda():
    while True:
        print("Escoja \n1.-Para buscar los partidos de un equipo especifico \n2.-Partidos en un estadio \n3.-Partidos en una fecha especifica \n4.-Salir")
        buscar = int(input("Ingrese el filtro por el que desea buscar:"))
        if buscar == 1:
            for team in Equipo.lista_equipos:
                team.mostrar_equipos()
            code = input("Ingrese el codigo del equipo que le interesa:").upper()
            equipo_objeto = Equipo.buscar_codigo(code)
            for match in Partido.lista_partidos:
                if match.local == equipo_objeto or match.visitante == equipo_objeto:
                    match.mostrar()

        elif buscar == 2:
            estad = int(input("Ingrese el id del estadio que le interesa:"))
            estadio_objeto = Estadio.buscar_id(estad)
            for match in Partido.lista_partidos:
                if match.estadio == estadio_objeto:
                    match.mostrar()

        elif buscar == 3:
            fecha = input("Ingrese la fecha que le interesa (MM/D/YYYY):")
            for match in Partido.lista_partidos:
                if match.fecha == fecha:
                    match.mostrar()

        elif buscar == 4:
            return
        else:
            print("Error, intente de nuevo")

def realizar_compra():
    print("*******BIENVENIDO********")
    cedula = int(input("Ingrese su cedula: "))
    cliente = Cliente.buscar_cedula(cedula)
    if cliente == None:
        nombre = input("Ingrese su nombre completo: ")
        edad = int(input("Ingrese su edad: "))
        Cliente.lista_clientes.append(Cliente(nombre, cedula, edad, []))
        print("Se ha creado su usuario, ingrese de nuevo a este menu para proceder con su compra.")
        return
    else:
        print(f"Hola {cliente.nombre}")
    confirmar = input("Desea comprar una entrada? (S/N): ").upper()
    while confirmar == "S":
        Partido.mostrar_compra()
        id_match = int(input("Ingrese el ID del partido que le interesa: "))
        partido_object = Partido.buscar_id(id_match)
        estadio_object = partido_object.estadio
        tipo_ticket = input("Cual entrada desea? (General/VIP): ")
        estadio_object.mostrar_mapa(partido_object)
        asiento = input("Ingrese el asiento que desea: ")
        if tipo_ticket == "VIP":
            monto = 120
        else:
            monto = 50
        recibo = {"Asiento": asiento, "Monto a pagar": monto , "Partido": partido_object.titulo()}
        for key, data in recibo.items():
            print(key, '-----', data)

        proceed = input("Desea proceder?: ")
        if proceed == "S":
            cliente.lista_compras.append(Compra(partido_object, asiento, tipo_ticket))
        confirmar = input("Desea realizar otra compra?")
    return

def compra_alimentos():
    cedula = int(input("Ingrese su cedula: "))
    cliente = Cliente.buscar_cedula(cedula)
    if len(cliente.lista_compras) > 1:
        for compra in cliente.lista_compras:
            compra.mostrar()
    print("En el orden dado, especifique el partido en el cual desea realizar su compra: ")
    espec = int(input('Partido: '))
    if cliente.lista_compras[espec-1].tipo_entrada != "VIP":
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
                for compra in client.lista_compras:
                    dicti = {"id del partido": (compra.partido).id, "asiento": compra.asiento,"tipo_entrada": compra.tipo_entrada}
                    lis_comp.append(dicti)
                lis_json.append({"nombre": client.nombre, "cedula": client.cedula, "edad": client.edad, "compras": lis_comp})
            json_str = json.dumps(lis_json)
            with open("Proyecto Algoritmo\clients.json", "w") as doc:
                doc.write(json_str)
            doc.close()
            break
    return

main()
