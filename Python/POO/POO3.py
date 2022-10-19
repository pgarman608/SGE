class Serie():
    def __init__(self,titulo="",numTemporadas=3,genero="",creador=""):
        self.titulo = titulo
        self.numTemporadas = numTemporadas
        self.entregado = False
        self.genero = genero
        self.creador = creador

    def setTitulo(self,titulo=""):
        self.titulo = titulo

    def setNumTemporadas(self,numTemporadas=3):
        self.numTemporadas = numTemporadas

    def setGenero(self,genero=""):
        self.genero = genero

    def setCreador(self,creador=""):
        self.creador = creador

    def getTitulo(self):
        return self.titulo

    def getNumTemporadas(self):
        return self.numTemporadas

    def getGenero(self):
        return self.genero

    def getCreador(self):
        return self.creador

    def toString(self):
        aux = "Serie: \nTitulo: " + self.titulo + "\nEntregado: " + self.entregado + "\nNumero de Temporadas: " + str(self.numTemporadas)
        aux += "\nGenero: " + self.genero + "\nCreador: " + self.creador
        return aux

    def entregar(self):
        self.entregado = True

class Videojuego():
    def __init__(self,titulo="",horasEstimadas=10,genero="",compania=""):
        self.titulo = titulo
        self.horasEstimadas=horasEstimadas
        self.entregado = False
        self.genero = genero
        self.compania = compania

    def setTitulo(self,titulo=""):
        self.titulo = titulo

    def setGenero(self,genero=""):
        self.genero = genero

    def setHorasEstimadas(self,horasEstimadas=10):
        self.horasEstimadas = horasEstimadas

    def setCompania(self,compania=""):
        self.compania = compania

    def getTitulo(self):
        return self.titulo

    def getGenero(self):
        return self.genero

    def getHorasEstimadas(self):
        return self.horasEstimadas

    def getCompania(self):
        return self.compania

    def toString(self):
        aux = "Videojuego: \nTitulo: " + self.titulo + "\nEntregado: " + self.entregado + "\nHoras Estimadas: " + str(self.horasEstimadas)
        aux += "\nGenero: " + self.genero + "\nCompania: " + self.compania
        return aux

    def entregar(self):
        self.entregado = True

"""Aplicacion de prueba"""

series = []
videojuegos = []

series.append(Serie())
series.append(Serie("Libro1",2,"Genero1","Creador1"))
series.append(Serie("Libro2",4,"Genero2","Creador2"))
series.append(Serie("Libro3",5,"Genero3","Creador3"))
series.append(Serie("Libro4",6,"Genero4","Creador4"))
series[1].entregar()
series[3].entregar()
videojuegos.append(Videojuego("Juego0"))
videojuegos.append(Videojuego("Juego1",20,"Genero1","Compania1"))
videojuegos.append(Videojuego("Juego2",4,"Genero2","Compania2"))
videojuegos.append(Videojuego("Juego3",5,"Genero3","Compania3"))
videojuegos.append(Videojuego("Juego4",6,"Genero4","Compania4"))
videojuegos[1].entregar()
videojuegos[2].entregar()
videojuegos[3].entregar()
countEV = 0
countES = 0
vjMash = videojuegos[0]
sMasT = series[0]
for i in range(5):
    if vjMash.getHorasEstimadas() < videojuegos[i].getHorasEstimadas():
        vjMash = videojuegos[i]
    if sMasT.getNumTemporadas() < series[i].getNumTemporadas():
        sMasT = series[i]
    if videojuegos[i].entregado == True:
        countEV += 1
    if series[i].entregado == True:
        countES += 1

print("Cantidad de juegos entregados: " + str(countEV))
print("Cantidad de series entregadas: " + str(countES))
print("Juego con mas horas estimadas: " + vjMash.getTitulo() + " con " + str(vjMash.getHorasEstimadas()))
print("Serie con mas temporadas: " + sMasT.getTitulo() + " con " + str(sMasT.getNumTemporadas()))
