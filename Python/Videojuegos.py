import pickle

class Videojuegos():
    def __init__(self):
        pick = open("videojuegos.txt","rb")
        self.Lista = pick.readlines()

    
    def alta(self,codigo="",nombre="",horas=""):
        error = 0
        print(self.Lista)
        if(len(self.Lista) == 0):
            self.Lista = [codigo,nombre,horas]
        else:
            if(not(codigo in self.Lista)):
                self.Lista.append([codigo,nombre,horas])
            else:

