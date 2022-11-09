# Funcion recursiva para exponencial

def exponencial(num, exp):
    if exp == 0:
        return 1

    return num * exponencial(num, exp - 1)

def busqueda(elem, lista, indice):
    if indice == len(lista):
        return
    elif lista[indice] == elem:
        return elem
    return busqueda(elem, lista, indice + 1)

def invertir_palabra(palabra, indice):
    if indice == 0:
        return palabra[indice]
    else:
        return palabra[indice] + invertir_palabra(palabra, indice -1)

def main():
    print("******PROGRAMA RECURSIVIDAD********")
    menu = int(input("Ingrese la accion que desea realizar \n1.-EXPONENCIAL \n2.-BUSCAR EN LISTA \n3.-INVERTIR UNA PALABRA"
                "\nINPUT:"))
    if menu == 1:
        print(exponencial(int(input("Numero:")), int(input("Elevado a: "))))
    elif menu == 2:
        lista = [1, 2, 3, 6, 4, 9, 10, 8]
        elemento = busqueda(int(input("Elemento: ")), lista, 0)
        if elemento == None:
            print("El elemento no se encuentra en la lista")
        else:
            print("El elemento si se encuentra en la lista")
    elif menu == 3:
        palabra = input("Ingrese la palabra:")
        print(invertir_palabra(palabra, len(palabra) - 1))

main()

