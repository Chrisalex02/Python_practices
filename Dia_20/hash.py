import numpy as np 

def frange(stop):#stop = posicion
    i=(stop+1)%10
    while i!=stop:#SI las posiciones se repiten se detiene el ciclo
        yield i
        i=(i+1)%10

def hashing(data):#Recibiendo los datos del usuario
    position=data%10#Residuo de la division del imput del usuario entre 10
    if a[position]==0:#Si la posicion 0 no esta ocupada
        a[position]=data#Guarda los datos en 0
    else:
        for i in frange(position):
            if a[i]==0:#Si el array en la posicion i todavia es 0
                a[i]=data#Reemplaza ese dato con el del usuario
                break

def busqueda(op):
    if(op=='S' or op=='s'):
        print("Introduca el numero a buscar")
        z=int(input("Valor: "))
        buscar(z)#Enviar consulta del usuario
        y=input("Desea buscar un elemento (S=si, N=no): ")
        busqueda(y)
    elif (op=='N' or 'n'):
        print("Fin")

def buscar(data):#Recibir consulta del usuario
    position=data%10#Revertir el cifrado del hash
    if a[position]==data:#Si lo que estaba en esa posicion es igual a lo que busca el usuario
        print("El elemento esta en el index: ", position+1)#Le digo donde esta guardado
    else:
        for i in frange(position):
            if a[i]==data:#Buscando en otras posiciones
                print("El elemento esta en el index: ", position+1)
                break
            if i==position:#No aparecio
                print("Elemento no encontrado")
                break

a=np.zeros(10)#Inicializando array: 10 valores en 0
print("Introduzca el arreglo: ")#Pedir datos
for i in range(0,10,1):#Rellenar datos
    x=int(input("Valor: "))#Recibir datos
    hashing(x)#Enviando datos a hashing
print(a)
y=input("Desea buscar un elemento (S=si, N=no): ")#Recibiendo lo que se desea buscar
busqueda(y)#Enviandolo al buscador