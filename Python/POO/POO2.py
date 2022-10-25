class Electrodoméstico():
    """El init de la clase"""
    def __init__(self,color="BLANCO",consumo="F",precio=100,peso=5):
        self.PRECIO = precio
        if self.__comprobarColor(color):
            self.COLOR = color
        else:
            self.COLOR = "BLANCO"
        self.CONSUMO = consumo
        self.PESO = peso
    """Getters del precio, color, consumo, Peso"""
    def getPRECIO(self):
        return self.PRECIO

    def getCOLOR(self):
        return self.COLOR

    def getCONSUMO(self):
        return self.CONSUMO

    def getPESO(self):
        return self.PESO
    """Comprobaremos que el nombre del consumo introducido si es correcto o no pasandolo por el return"""
    def __comprobarConsumoEnergetico(self,consumo):
        aux = True
        if "A" != str.upper(consumo) and "B" != str.upper(consumo) and "C" != str.upper(consumo) and "D" != str.upper(consumo) and "E" != str.upper(consumo) and "F" != str.upper(consumo):
            aux = False
        return aux
    """Comprobaremos que el color del electrodomestico es correcto o no pasandolo por el return"""
    def __comprobarColor(self,color):
        aux = True
        if "BLANCO" != str.upper(color) and "NEGRO" != str.upper(color) and "ROJO" != str.upper(color) and "AZUL" != str.upper(color) and "GRIS" != str.upper(color):
            aux = False
        return aux
    """Calcularemos el precio final y lo pasaremos por el return"""
    def precioFinal(self):
        consumo = 0
        if "A" == self.CONSUMO:
            consumo = 100
        elif "B" == self.CONSUMO:
            consumo = 80
        elif "C" == self.CONSUMO:
            consumo = 60
        elif "D" == self.CONSUMO:
            consumo = 50
        elif "E" == self.CONSUMO:
            consumo = 30
        elif "F" == self.CONSUMO:
            consumo = 10
        tamanio = 0
        if self.PESO >= 0 and self.PESO <= 19:
            tamanio = 10
        elif self.PESO >= 20 and self.PESO <= 49:
            tamanio = 50
        elif self.PESO >= 50 and self.PESO <= 79:
            tamanio = 80
        elif self.PESO >= 80:
            tamanio = 100
        return self.PRECIO + tamanio + consumo

class Lavadora(Electrodoméstico):
    """El init de la clase"""
    def __init__(self, color="BLANCO", consumo="F", precio=100, peso=5, carga=5):
        super().__init__(color, consumo, precio, peso)
        self.CARGA = carga
    """Getter de la carga"""
    def getCARGA(self):
        return self.CARGA
    """Calcularemos el precio final de la lavadora pasandolo por el return"""
    def precioFinal(self):
        carga = 0
        if self.CARGA >=30:
            carga = 50
        return super().precioFinal() + carga

class Television(Electrodoméstico):
    """El init de la clase"""
    def __init__(self, color="BLANCO", consumo="F", precio=100, peso=5,resolucion=20,fourK=False):
        super().__init__(color, consumo, precio, peso)
        self.RESOLUCION = resolucion
        self.FOURK = fourK
    """Getter de la resolucion y del 4k"""
    def getRESOLUCION(self):
        return self.RESOLUCION

    def getFOURK(self):
        return self.FOURK
    """Calcularemos el precio final de la television pasandolo por el return"""
    def precioFinal(self):
        resolucion  = 1.00
        if self.RESOLUCION >= 40:
            resolucion = 1.30
        fourk = 0
        if self.FOURK is True:
            fourk = 50
        return (super().precioFinal() * resolucion) + fourk

class Ejecutable():
    """El init de la clase"""
    def __init__(self):
        self.electrodomesticos = []
        self.electrodomesticos.append(Electrodoméstico())
        self.electrodomesticos.append(Electrodoméstico("negro","A",200,20))
        self.electrodomesticos.append(Electrodoméstico("rojo","B",250,30))
        self.electrodomesticos.append(Electrodoméstico("azul","C",150,40))
        self.electrodomesticos.append(Lavadora())
        self.electrodomesticos.append(Lavadora("negro","D",250,50,20))
        self.electrodomesticos.append(Lavadora("rojo","E",150,60,50))
        self.electrodomesticos.append(Television())
        self.electrodomesticos.append(Television("azul","F",250,70,30,True))
        self.electrodomesticos.append(Television("gis","A",150,80,50,False))
    """Veremos los precios de la lista de electrodomesticos y lo pasaremos por el return"""
    def verPrecios(self):
        countE = 0
        countL = 0
        countT = 0
        for electrodomestico in self.electrodomesticos:
            print(type(electrodomestico))
            if isinstance(electrodomestico,Lavadora):
                countL += 1
                aux = aux + "\nLavadora "+str(countL)+": " + str(electrodomestico.precioFinal())
            elif isinstance(electrodomestico,Television):
                countT += 1
                aux = aux + "\nTelevision "+str(countT)+": " + str(electrodomestico.precioFinal())
            elif isinstance(electrodomestico,Electrodoméstico) :
                countE += 1
                aux = aux + "\nElectrodomestico "+str(countE)+": " + str(electrodomestico.precioFinal())
                print()
        return aux

prueba = Ejecutable()
print(prueba.verPrecios())
