#Estoy seguro de que esto es una mala practica, pero asi se queda por hoy
def main():
    seleccion = input("Prsione 1 para circulo, 2 para triangulo o 3 para cuadrado: ")
    seleccion = str(seleccion)

    if seleccion == "1":
        from Figuras.circulo import circulo 

    elif seleccion == "2":
        from Figuras.triangulo import triangulo

    elif seleccion == "3":
        from Figuras.cuadrado import cuadrado

    else:
        print("Opcion invalida")
        main()

main()
    
