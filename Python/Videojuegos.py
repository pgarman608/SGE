import pickle
import os
from Videojuego import Videojuego
class Videojuegos():
    def __init__(self):
        pick = open("videojuegos.txt","rb")
        file = "videojuegos.txt"
        filecomp = os.stat(file)
        self.tamanioFichero = filecomp.st_size
        if self.tamanioFichero != 0:
            self.Lista = pickle.load(pick)
            pick.close()
        else:
            self.Lista = []

    def alta(self,codigo="",nombre="",genero=""):
        error = 0
        if len(self.Lista) == 0 :
            self.Lista = [Videojuego(codigo, nombre, genero)]
        else:
            if(self.comprobarCodigo(codigo)):
                self.Lista.append(Videojuego(codigo, nombre, genero))
            else:
                error = -1
        return error

    def exportarVideojuegos(self):
        pick = open("videojuegos.txt","wb")
        pickle.dump(self.Lista, pick)
        pick.close()

    def comprobarCodigo(self,codigo):
        comp = True
        for i in range(len(self.Lista)):
            if self.Lista[i].codigo == codigo:
                comp = False
        return comp

    def eliminarVideojuego(self,codigo):
        if len(self.Lista)-1 == 0:
            listaeliminar = self.Lista[0]
            self.Lista.remove(listaeliminar)
        for i in range(len(self.Lista)-1):
            if self.Lista[i][0] == codigo:
                videojuegoEliminar = self.Lista[i]
                self.Lista.remove(videojuegoEliminar)

    def buscarVideojuego(self,codigo):
        videojuegoRecorer = Videojuego(codigo, nombre="", genero="")
        if len(self.Lista)-1 == 0:
            listarecoger = self.Lista[0]
        for i in range(len(self.Lista)-1):
            if self.Lista[i].codigo == codigo:
                videojuegoRecorer = self.Lista[i]
        return videojuegoRecorer.nombre, videojuegoRecorer.genero
    def modificarVideojuego(self,codigo,nombre,genero):
        if len(self.Lista)-1 == 0:
            if self.Lista[0].codigo == codigo:
                self.Lista[0].nombre = nombre
                self.Lista[0].genero = genero
        for i in range(len(self.Lista)-1):
            if self.Lista[0].codigo == codigo:
                self.Lista[0].nombre = nombre
                self.Lista[0].genero = genero