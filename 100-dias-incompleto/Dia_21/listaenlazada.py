#Definiendo el nodo
class Nodo():
    dato = None
    siguiente = None

    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None#"Apuntador"

def agregar_final(nodo_inicial,dato):
    nuevo_nodo = Nodo(dato)#Crear un nuevo nodo
    if nodo_inicial == None:#La lista esta vacia
        nodo_inicial = nuevo_nodo
        return nodo_inicial
    
    temporal = nodo_inicial#La lista no esta vacia
    while temporal.siguiente:#Si hay algo en ese nodo
        temporal = temporal.siguiente#Voy pasando hasta llegar al ultimo
    temporal.siguiente = nuevo_nodo#Llego al ultimo y pongo algo nuevo
    return nodo_inicial

def agregar_inicio(nodo_inicial,dato):#Reemplazar el primero
    nuevo_nodo = Nodo(dato)#crear nuevo nodo
    nuevo_nodo.siguiente = nodo_inicial#El que antes era el inicial ahora es el siguiente
    return nuevo_nodo

def imprimir_lista(nodo):#Mostrar todos los nodos
    while nodo != None:#LLegar hasta el ultimo nodo
        texto = "Tenemos {}"
        print(texto.format(nodo.dato))#Imprimir todos los nodos
        nodo = nodo.siguiente#Seguir avanzando hasta el ultimo
    

def obtener_cabeza(nodo_inicial):
    return nodo_inicial#Devolver el inicial

def obtener_cola(nodo_inicial):
    temporal = nodo_inicial#Cual es el primero
    while temporal.siguiente:#Mientras haya otros
        temporal = temporal.siguiente#seguir avanzando hasta que no haya mas
    return temporal#Mostrar el ultimo

def existe(nodo, busqueda):
    while nodo != None:#Revisar la lista
        if nodo.dato == busqueda:#Si el nodo tiene el dato que busco
            return "True"#Me detengo 
        nodo = nodo.siguiente#Si no lo tiene continuo
    return "False"#no lo encontro

def eliminar(nodo, busqueda):
    if nodo == None:
        return
    if nodo.dato == busqueda:
        return nodo.siguiente
    temporal = nodo
    while temporal.siguiente != None:
        if temporal.siguiente.dato == busqueda:
            if temporal.siguiente.siguiente !=None:
                temporal.siguiente = temporal.siguiente.siguiente
            else:
                temporal.siguiente = nodo
                return nodo
        temporal = temporal.siguiente
    return nodo

def main():
    lista = None
    lista = agregar_final(lista, "Luis")
    lista = agregar_inicio(lista, "Dayana")
    lista = agregar_final(lista, "Ariangel")
    print("Antes de eliminar: ")
    imprimir_lista(lista)
    eliminar(lista, "Ariangel") #Luego de eliminar se genera un bucle infinito
    print("Despues de eliminar: ")
    #imprimir_lista(lista) #Se vuelve un bucle infinito
    print(existe(lista, "Ariangel"))#No lo ejecuta
    print(existe(lista, "Luis"))#No lo ejecuta
    print(obtener_cabeza(lista).dato)#No lo ejecuta
    print(obtener_cola(lista).dato)#No lo ejecuta

main()

