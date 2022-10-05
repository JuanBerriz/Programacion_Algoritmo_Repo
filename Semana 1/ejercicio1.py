#Ejercicio 5

# horas = int(input("Ingrese la cantidad de horas que trabajó: "))

# monto = int(input("Ingrese el monto que cobra por hora: "))

# print(f"Usted deberia cobrar {horas*monto} $")

#Ejercicio 11

def porcentaje(num):
    ahorrado = round(num + (num*4)/100, 2)
    return ahorrado

ahorro_inicial = float(input("Ingrese la cantidad de dinero inicial en la cuenta de ahorro: "))

ahorro_1 = porcentaje(ahorro_inicial)

ahorro_2 = porcentaje(ahorro_1)

ahorro_3 = porcentaje(ahorro_2)

print(f"En el primer año, habrá ahorrado {ahorro_1}, en el segundo {ahorro_2} y el tercero {ahorro_3}")