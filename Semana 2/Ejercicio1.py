#Ejercicio 1 Semana 2 Lunes

def prevencion():
    while True:
        try:
            num = float(input("Ingresar un numero distinto de cero:"))
        except ValueError:
            print("Valor invalido, ingrese de nuevo:")
        else:
            break
    return num


n1 = prevencion()
n2 = prevencion()

while n1 != 0:

    if n1%2 == 0:
        print(f"{n1} es par.")
    else:
        print(f"{n1} es impar.")

    if n2 != 0:
        print("La division de ambos numeros es ", n1/n2)
    else:
        print("Error, el segundo numero es un cero")

    n1 = prevencion()
    if n1 == 0:
        break
    n2 = prevencion()

print("Programada terminado.")
