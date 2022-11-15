import pickle
import os
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

    def alta(self,codigo="",nombre="",Genero=""):
        error = 0
        if(len(self.Lista) == 0 or len(self.Lista[0]) == 0):
            self.Lista = [[codigo,nombre,Genero]]
        else:
            if(self.comprobarCodigo(codigo)):
                self.Lista.append([codigo,nombre,Genero])
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
            if self.Lista[i][0] == codigo:
                comp = False
        return comp

    def eliminarVideojuego(self,codigo):
        if len(self.Lista)-1 == 0:
            listaeliminar = self.Lista[0]
            self.Lista.remove(listaeliminar)
        for i in range(len(self.Lista)-1):
            if self.Lista[i][0] == codigo:
                listaeliminar = self.Lista[i]
                self.Lista.remove(listaeliminar)

    def buscarVideojuego(self,codigo):
        listarecoger = []
        if len(self.Lista)-1 == 0:
            listarecoger = self.Lista[0]
        for i in range(len(self.Lista)-1):
            if self.Lista[i][0] == codigo:
                listarecoger = self.Lista[i]
        return listarecoger[1],listarecoger[2]

    def modificarVideojuego(self,codigo,nombre,Genero):
        if len(self.Lista)-1 == 0:
            if self.Lista[0][0] == codigo:
                self.Lista[0][1] = nombre
                self.Lista[0][2] = Genero
        for i in range(len(self.Lista)-1):
            if self.Lista[i][0] == codigo:
                self.Lista[i][1] = nombre
                self.Lista[i][2] = Genero