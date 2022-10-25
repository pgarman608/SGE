class Punto:
    x = 0
    y = 0
    """El init de la clase"""
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        pass
    """Pasaremos todos los metodos como si fuesen un String"""
    def toString(self):
        return "X: " + str(self.x) + " e Y: " + str(self.y)

class Forma:
    __color = ""
    coord = Punto()
    nombre = ""
    """El init de la clase"""
    def __init__(self, color = "", x= 0,y = 0,nombre = ""):
        self.coord = Punto(x,y)
        self.__color = color
        self.nombre = nombre
    """Pasaremos todos los metodos como si fuesen un String"""
    def toString(self):
        return "Nombre: " + self.nombre + "\nCoordenadas: " + self.coord.toString() + "\nColor: "+ self.__color
    """Setter del color"""
    def setColor(self,color=""):
        self.__color = color
    """Getter del color"""
    def getColor(self):
        return self.__color
    """Setter de las coordenadas"""
    def setCoord(self,x=0,y=0):
        self.coord = Punto(x,y)

class Rectangulo(Forma):
    lMenor = 0
    lMayor = 0
    """El init de la clase"""
    def __init__(self, color="", x=0, y=0, nombre="",lMenor = 2,lMayor = 1):
        super().__init__(color, x, y, nombre)
        self.lMayor = lMayor
        self.lMenor = lMenor
        pass
    """Pasaremos todos los metodos como si fuesen un String"""
    def toString(self):
        return super().toString() + "\nLado menor: " + str(self.lMenor) + "\nLado mayor: " +  str(self.lMayor)
    """Pasaremos el area calculada del Rectrangulo"""
    def area(self):
        resul = self.lMayor * self.lMenor
        return resul
    """Pasaremos el perimetro por el return"""
    def perimetro(self):
        resul = self.lMayor * 2 + self.lMenor * 2
        return resul
    """Cambiamos el tamaño de los lados"""
    def cambiarTamanio(self,numero = 1):
        self.lMenor = self.lMenor * numero
        self.lMayor = self.lMayor * numero
"""
forma = Forma("Blanco",20,10,"Edificio1")
print(forma.toString())
forma.setColor("Azul")
print(forma.getColor())
forma.setCoord(10,20)
print(forma.toString())
rectangulo = Rectangulo("Negro",10,10,"marco",10,10)
print(rectangulo.toString())
rectangulo.setColor("Amarillo")
print(rectangulo.getColor())
rectangulo.setCoord(30,40)
rectangulo.cambiarTamanio(4)
print(rectangulo.toString())
print(rectangulo.area())
print(rectangulo.perimetro())
"""
class Elipse(Forma):
    rMayor = 0
    rMenor = 0
    PI = 3.1416
    """El init de la clase"""
    def __init__(self, color="", x=0, y=0, nombre="",rMayor = 2,rMenor=1):
        super().__init__(color, x, y, nombre)
        self.rMayor = rMayor
        self.rMenor = rMenor
    """Pasaremos todos los metodos como si fuesen un String"""
    def toString(self):
        return super().toString() + "\nRadio Mayor: " + str(self.rMayor) +"\nRadio Menor: " + str(self.rMenor)
    """Devolveremos el area del Elipse"""
    def area(self):
        return self.PI * (self.rMayor * self.rMenor)

class Cuadrado(Rectangulo):
    """El init de la clase"""
    def __init__(self, color="", x=0, y=0, nombre="", lado = 1):
        super().__init__(color, x, y, nombre, lado, lado)
    """Pasaremos todos los metodos como si fuesen un String"""
    def toString(self):
        return "Nombre: " + self.nombre + "\nCoordenadas: " + self.coord.toString() + "\nColor: "+ self.getColor() + "\nLado: " + str(self.lMayor)

class Circulo(Elipse):
    """El init de la clase"""
    def __init__(self, color="", x=0, y=0, nombre="", radio = 1):
        super().__init__(color, x, y, nombre, radio, radio)
    """Pasaremos todos los metodos como si fuesen un String"""
    def toString(self):
        return "Nombre: " + self.nombre + "\nCoordenadas: " + self.coord.toString() + "\nColor: "+ self.getColor() + "\nRadio: " + str(self.rMayor)

"""Programa de prueba"""
listaFiguras = list()
forma = Forma("negro",10,10,"Edificio")
rectangulo = Rectangulo("negro",10,10,"Campo",30,20)
cuadrado = Cuadrado("negro",10,10,"Hectarea",10)
elipse = Elipse("negro",10,10,"Tierra",10,9)
circulo = Circulo("negro",10,10,"Pelota",7)
listaFiguras.append(forma)
listaFiguras.append(rectangulo)
listaFiguras.append(cuadrado)
listaFiguras.append(elipse)
listaFiguras.append(circulo)

for figura in listaFiguras:
    print(figura.toString())
    figura.setColor("rojo")
    figura.setCoord(20,20)
    print(".-.-.")
    print(figura.toString())
    print("-----------------")