#import opciones

def cuadrado():
    #opcion = opciones.opciones()
    print("Escriba \"area\" o \"perimetro\" para seleccionar la operacion que desea realizar")
    print("O presione 1 para calcular el area y 2 para calcular el perimetro")
    opcion = input("Indique que desea calcular: ")
    opcion = str(opcion)
    opcion = opcion.lower()

    if opcion == "1" or opcion == "area":
        def area_cuadrado():
            l = input("Indique la longitud de uno de los lados: ")
            l = int(l)
            print(l**2)
        
        area_cuadrado()
    
    elif opcion == "2" or opcion == "perimetro":
        def perimetro_cuadrado():
            l = input("Indique la longitud de uno de los lados: ")
            l = int(l)
            print(l*4)

        perimetro_cuadrado()

    else:
        print("La opcion que ingreso no es valida, intentelo nuevamente")
        cuadrado()

cuadrado()