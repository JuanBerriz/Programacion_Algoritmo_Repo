#Recursividad Busqueda

def busqueda(elem, lista, indice):
    if indice == len(lista):
        return
    elif lista[indice] == elem:
        return elem
    return busqueda(elem, lista, indice + 1)

def main():
    lista = [1, 2, 3, 6, 4, 9, 10, 8]
    elemento = busqueda(int(input("Elemento: ")), lista, 0)
    if elemento == None:
        print("El elemento no se encuentra en la lista")
    else:
        print("El elemento si se encuentra en la lista")

main()