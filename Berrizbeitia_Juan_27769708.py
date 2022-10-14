#Problema 2

def input_menu():
    while True:
        try:
            menu = int(input("Acción:"))
            if menu <= 0 or menu >= 5:
                raise Exception
            return menu
        except:
            print("Acción no válida\n")

def input_cedula():
    cedula = input("Cédula:")
    x = [num for num in cedula[-3:]]
    verificar = int(("".join(x)))
    for num in range(2, verificar):
        if verificar%num == 0:
            descuento = 1
        else:
            descuento = 0.9
    return cedula, descuento

def input_id():
    while True:
        try:
            id = int(input("ID del juego:"))
            if id <= 0 or id >= 9:
                raise Exception
            return id
        except:
            print("Error, intente de nuevo\n")

def estadisticas(id_compra, estadistica):
    for games in estadistica:
        for key,value in games.items():
            if key == "id" and value == id_compra:
                games["Cantidad Vendida"] += 1
    return estadistica


def main():
    
    juegos = {
    "Shooter": [
        {
            "id": 1,
            "name": "Overwatch2",
            "price": 60  
        },
        {
            "id": 2,
            "name": "Valorant",
            "price": 0
        },
        {
            "id": 3,
            "name": "Pixel Gun 3D",
            "price": 10
        }
    ],
    "RPG": [
        {
            "id": 4,
            "name": "Pokemon",
            "price": 50  
        },
        {
            "id": 5,
            "name": "Final Fantasy Exvius",
            "price": 0
        }
    ],
    "Open World": [
        {
            "id": 6,
            "name": "Minecraft",
            "price": 60  
        },
        {
            "id": 7,
            "name": "Cyberpunk 2077",
            "price": 60
        },
        {
            "id": 8,
            "name": "GTA V",
            "price": 40
        }
        ],  
    }

    estadistica = [
        {
        "id": 1,
        "name": "Overwatch2",
        "Cantidad Vendida": 0  
        },

        {
        "id": 2,
        "name": "Valorant",
        "Cantidad Vendida": 0
        },

        {
        "id": 3,
        "name": "Pixel Gun 3D",
        "Cantidad Vendida": 0 
        },

        {
        "id": 4,
        "name": "Pokemon",
        "Cantidad Vendida": 0  
        },

        {
        "id": 5,
        "name": "Final Fantasy Exvius",
        "Cantidad Vendida": 0 
        },

        {
        "id": 6,
        "name": "Minecraft",
        "Cantidad Vendida": 0  
        },
        
        {
        "id": 7,
        "name": "Cyberpunk 2077",
        "Cantidad Vendida": 0 
        },

        {
        "id": 8,
        "name": "GTA V",
        "Cantidad Vendida": 0 
        } 
    ]

    print("***********======BIENVENIDO=======***********")
    while True:

        print("Ingrese la acción que desea realizar:\n1-Ver directorio de juegos \n2-Realizar compra \n3-Estadísticas \n4-Salir \n")
        menu = input_menu()

        if menu == 1:
            for genre, games in juegos.items():
                print(f"{genre} \n")
                for dict in games:
                    for key,info in dict.items():
                        if key == "price" and info == 0:
                            info = "GRATIS"
                        print("     ",key," ---- ",info)
                        if key =="price":
                            print("")

        elif menu == 2:
            nombre = input("Ingrese su nombre y apellido: ")
            cedula, descuento = input_cedula()
            id_compra = input_id()
            for genre, games in juegos.items():
                for dict in games:
                    for key, info in dict.items():
                        if key == "id":
                            if id_compra == info:
                                juego_comprar = dict
        
            print("Confirmar que es el juego que desea.")
            for key, info in juego_comprar.items():
                if key == "price" and info == 0:
                            info = "GRATIS"
                print(key," ---- ",info)
            confirmar = input("S para seguir adelante, N para eliminar la compra (Nota: Si escribe N, se regresará al menú principal: ")
            if confirmar.lower() == "s":
                estadisticas(id_compra, estadistica)
                if descuento == 0.9:
                    print("Felicidades, aplica para un descuento del 10% en su compra final, se aplicará automaticamente")
                factura = {
                    "Nombre": nombre,
                    "Cedula": cedula,
                    "Juego": juego_comprar["name"],
                    "Precio": juego_comprar["price"]*descuento
                }
                print("Su total es:")
                for key, info in factura.items():
                    if key == "Precio" and info == 0:
                            info = "GRATIS"
                    print("    ",key, " --- ", info)
                print('')
            else:
                continue

        elif menu == 3:
            for games in estadistica:
                for key, value in games.items():
                    if key == "id":
                        continue
                    print("   ", key," ---- ",value)
                    if key =="Cantidad Vendida":
                            print("")
        elif menu == 4:
            print("Muchas gracias y que tenga un buen día")
            break

main()