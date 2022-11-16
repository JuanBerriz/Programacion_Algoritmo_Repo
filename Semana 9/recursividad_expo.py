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

def orden_numeros(lista, indice, contador):
    if indice == len(lista)-1:
        if contador == len(lista):
            return lista
        else:
            indice = 0
            return orden_numeros(lista, indice, contador + 1)
    actual = lista[indice]
    siguiente = lista[indice+1]
    if actual > siguiente:
        lista[indice] = siguiente
        lista[indice+1] = actual
    
    return orden_numeros(lista, indice + 1, contador)
    

def main():
    print("******PROGRAMA RECURSIVIDAD********")
    menu = int(input("Ingrese la accion que desea realizar \n1.-EXPONENCIAL \n2.-BUSCAR EN LISTA \n3.-INVERTIR UNA PALABRA"
                "\n4.-Ordenar numeros de una lista \nINPUT: "))
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
    elif menu == 4:
        lista = [9, 1, 13, 2, 47, 6, 4, 10, 8, 99, 26, 83]
        
        print(orden_numeros(lista, 0, 1))
    else:
        print("Error, Hasta Luego")

main()

