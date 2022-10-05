#Ejercicio 3 Semana 2 Lunes
while True:
    tipo =input("Ingresar el tipo de pizza que quiere, V siendo vegetariana y N no vegetariana:").upper()
    if tipo != "V" and tipo !="N":
        print("Ingreso invalido, intente de nuevo")
    else:
        break

if tipo == "V":
    ingredientes = ["Tofu", "Pimiento"]
else:
    ingredientes = ["Peperoni", "Jamon", "Salmon"]

print("A continuacion tiene los ingredientes disponibles para añadir a su pizza:", ingredientes)
seleccion = int(input(f"Seleccione uno de los ingredientes, siendo 0 el primero y {len(ingredientes)-1}, el ultimo:"))

if tipo == "V":
    print("Usted selecciono la pizza vegetariana")
    print(f"Con la adicion de {ingredientes[seleccion]}")
else:
    print("Usted selecciono la pizza no vegetariana")
    print(f"Con la adicion de {ingredientes[seleccion]}")
