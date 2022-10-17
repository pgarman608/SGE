class Punto:
    x
    y
    def __init__(self):
        self.x = 0
        self.y = 0
    def __int__(self,x,y):
        self.x = x
        self.y = y
    def toString(self):
        return "X: " + self.x + "e Y:" + self.y
class Forma:
    __color
    coord
    nombre
    def __init__(self):
        self.color = ""
        self.coord = Punto()
        self.nombre = ""
    def __init__(self, color, x,y,nombre):
        self.coord = Punto(x,y)
        self.color = color
        self.nombre = nombre
    def toString(self):
        return "Nombre: " + self.nombre + "\nColor: " + self.color + "\nCoordenadas: " + self.coord.toString()
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def setCoord(self,x,y):
        self.coord = Punto(x,y)
class Rectangulo(Forma):
    lMenor
    lMayor
    def __init__(self):
        super()
        self.lMenor = 0
        self.lMayor = 0
    def __int__(self,color,x,y,nombre,lMenor,LMayor):
        super(Rectangulo, self).__int__(color,x,y,nombre)
        self.lMenor = lMenor
        self.lMayor = LMayor
    def toString(self):
        return "Nombre: " + self.nombre + "\nColor: " + self.color + "\nCoordenadas: " + self.coord.toString() + "\nLado Menor: " + self.lMenor + "\nLado Mayor: " + self.lMayor
if __name__ == '__main__':
    rectangulo = Rectangulo("Negro",10,10,"Campo","10","15")
    print(rectangulo.toString())