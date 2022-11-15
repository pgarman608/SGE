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

    def alta(self,codigo="",nombre="",horas=""):
        error = 0
        if(len(self.Lista) == 0 or len(self.Lista[0]) == 0):
            self.Lista = [[codigo,nombre,horas]]
        else:
            if(self.comprobarCodigo(codigo)):
                self.Lista.append([codigo,nombre,horas])
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
        for i in range(len(self.Lista)):
            if self.Lista[i][1] == codigo:
                listaeliminar = self.Lista[i]
                self.Lista.remove(listaeliminar)