class Drink:
    def __init__(self, name):#Metodo constructor
        self.__name = name #El doble piso lo hace privado self.name == publico 

    def getDetail(self):
        return "La bebida es: " + self.__name #self.__name == privado solo accesible desde metodos

class Product:
    def __init__(self, price, cost):
        self.cost = cost
        self.price = price
    
    def detGain():
        return self.price - self.cost

class Beer(Drink, Product):#Herencia
    #Con herencia multiple se cambia el super() por el nombre de la clase
    Count = 0 #Metodo estatico, accesible sin instanciar

    def __init__(self, name, brand, alcohol, cost, price): #Recrear el constructor padre
        Drink.__init__(self, name)#Llamar al constructor padre y pasarle el nuevo dato desde el hijo
        #De lo contratio da error
        Product.__init__(self, price, cost)#Con herencia multiple se pasa el self para evitar conflgitictos
        self.__brand = brand
        self.__alcohol = alcohol
        Beer.Count += 1 #Contador de intancias de clase, accesible desde todas las instancias

    def getDetail(self):
        return "La bebida es: " + self.__name #si dos metodos se llaman igual el metodo se sobre ecribe
        #es decir se escoge el metodo del propio objeto

    @staticmethod
    def detClassInfo(): #Metodo estatico ejecutable directamente
        return "Se a creado " + str(Beer.Count) + " objetos"

drink = Drink("agua")
#print(drink.name)#Si coloco el nombre de la clase "Drink.name" da error
print(drink.getDetail())