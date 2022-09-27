import numpy as np 

def frange(stop):
    i=(stop+1)%10
    while i!=stop:
        yield i
        i=(i+1)%10

def hashing(data):
    position=data%10
    if a[position]==0:
        a[position]=data
    else:
        for i in frange(position):
            if a[i]==0:
                a[i]=data
                break

def busqueda(op):
    if(op=='S' or op=='s'):
        print("Introduca el numero a buscar")
        z=int(input("Valor: "))
        buscar(z)
        y=input("Desea buscar un elemento (S=si, N=no): ")
        busqueda(y)
    elif (op=='N' or 'n'):
        print("Fin")

def buscar(data):
    position=data%10
    if a[position]==data:
        print("El elemento esta en el index: ", position+1)
    else:
        for i in frange(position):
            if a[i]==data:
                print("El elemento esta en el index: ", position+1)
                break
            if i==position:
                print("Elemento no encontrado")
                break

a=np.zeros(10)
print("Introduzca el arreglo: ")
for i in range(0,10,1):
    x=int(input("Valor: "))
    hashing(x)
print(a)
y=input("Desea buscar un elemento (S=si, N=no): ")
busqueda(y)