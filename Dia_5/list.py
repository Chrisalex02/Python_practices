import pprint #paquete pretty print

#Creando lista 3D, definir una funcion para introducir los datos de cada lista
def tresD(a, b , c):
    #creando lista con bucles en cada culumna y fila
    lista = [[['#' for col in range(a)] for col in range(b)] for row in range(c)]
    return lista

#usando pretty print
#pprint.pprint(tresD(5, 3, 2))

def tresD(a, b , c):
    #creando lista con bucles en cada culumna y fila
    lista1 = [[['1' for col in range(a)] for col in range(b)] for row in range(c)]
    lista2 = [[['2' for col in range(a)] for col in range(b)] for row in range(c)]
    #Mezclando con el operador +
    lista = lista1 + lista2
    return lista

#pprint.pprint(tresD(5, 3, 2))

#factorial
#Crear una funcion con "n" = limite del factorial
def factorial(n, a=1):
    lista3 = ['basura' for i in range(n)]
    for j in range(len(lista3)):
        a+=1
    print(a*n)

n = 5
factorial(n)
