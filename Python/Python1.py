from cmath import rect
import re


class Punto:
    x = 0
    y = 0
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        pass
    def toString(self):
        return "X: " + str(self.x) + " e Y: " + str(self.y)

class Forma:
    __color = ""
    coord = Punto()
    nombre = ""
    def __init__(self, color = "", x= 0,y = 0,nombre = ""):
        self.coord = Punto(x,y)
        self.__color = color
        self.nombre = nombre

    def toString(self):
        return "Nombre: " + self.nombre + "\nCoordenadas: " + self.coord.toString() + "\nColor: "+ self.__color

    def setColor(self,color=""):
        self.__color = color

    def getColor(self):
        return self.__color

    def setCoord(self,x=0,y=0):
        self.coord = Punto(x,y)

class Rectangulo(Forma):
    lMenor = 0
    lMayor = 0
    def __init__(self, color="", x=0, y=0, nombre="",lMenor = 1,lMayor = 1):
        super().__init__(color, x, y, nombre)
        self.lMayor = lMayor
        self.lMenor = lMenor
        pass
    def toString(self):
        aux = "Nombre: " + self.nombre + "\nCoordenadas: " + self.coord.toString() + "\nColor: " + self.getColor() + "\nLado menor: " + str(self.lMenor) + "\nLado mayor: " +  str(self.lMayor)
        return aux
    def area(self):
        resul = self.lMayor * self.lMenor
        return resul
    def perimetro(self):
        resul = self.lMayor * 2 + self.lMenor * 2
        return resul
    def cambiarTamanio(self,numero = 1):
        self.lMenor = self.lMenor * numero
        self.lMayor = self.lMayor * numero

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