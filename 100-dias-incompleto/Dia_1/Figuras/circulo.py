#Dejare todos los comentarios para valuar mi progreso
#d = input("Ingrese el diametro del circulo: ")

#import opciones

Pi = 3.1416
def circulo():
    print("Escriba \"area\" o \"perimetro\" para seleccionar la operacion que desea realizar")
    print("O presione 1 para calcular el area y 2 para calcular el perimetro")
    opcion = input("Indique que desea calcular: ")
    opcion = str(opcion)
    #print(type(opcion))
    opcion = opcion.lower()
    #print(opcion)

    #opcion = opciones.opciones()

    if opcion == "1" or opcion == "area":
        def area_circulo():
            r = int(input("Ingrese el radio del circulo: "))
            #print(r)
            #print(type(r))
            print(Pi * r**2) 

        area_circulo()
    elif opcion == "2" or opcion == "perimetro":
        def perimetro_circulo():
            r = int(input("Ingrese el radio del circulo: "))
            print(2*r * Pi)

        perimetro_circulo()
    
    else:
        print("La opcion que ingreso no es valida, intentelo nuevamente")
        circulo()

circulo()