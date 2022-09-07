#import opciones

def triangulo():
    #opcion = opciones.opciones() Pide opciones dos veces ¿Por que?
    print("Escriba \"area\" o \"perimetro\" para seleccionar la operacion que desea realizar")
    print("O presione 1 para calcular el area y 2 para calcular el perimetro")
    opcion = input("Indique que desea calcular: ")
    opcion = str(opcion)
    opcion = opcion.lower()

    if opcion == "1" or opcion == "area":
        def area_triangulo():
            l1 = int(input("Ingrese el primer lado del triangulo: "))
            l2 = int(input("Ingrese el segundo lado del triangulo: "))
            l3 = int(input("Ingrese el tercer lado del triangulo: "))
            print(l1 + l2 + l3)

        area_triangulo()

    elif opcion == "2" or opcion == "perimetro":
        def perimetro_triangulo():
            b = int(input("Ingrese la base del triangulo: "))
            h = int(input("Ingrese la altura del triangulo: "))
            producto = b * h
            print(producto / 2)

        perimetro_triangulo()

    else:
        print("La opcion que ingreso no es valida, intentelo nuevamente")
        triangulo()

triangulo()