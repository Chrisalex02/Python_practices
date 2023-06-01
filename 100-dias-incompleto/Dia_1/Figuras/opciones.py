def opciones():
    print("Escriba \"area\" o \"perimetro\" para seleccionar la operacion que desea realizar")
    print("O presione 1 para calcular el area y 2 para calcular el perimetro")
    opcion = input("Indique que desea calcular: ")
    opcion = str(opcion)
    opcion = opcion.lower()
    return opcion

opciones()