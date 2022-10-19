from random import Random

class Persona():
    def __init__(self,nombre="",edad=0,peso=0,altura=0,sexo="M"):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = self.__generarDNI()
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo

    def calcularMC(self):
        return self.__peso * (self.__altura^2)

    def esMayorDeEdad(self):
        aux = "Es mayor de edad"
        if(self.__edad < 18):
            aux = "Es menor de edad"
        return aux

    def introducirSexo(self,sexo):
        if(str.upper(sexo)== "H"):
            self.__sexo = "H"

    def toString(self):
        aux = "Nombre: " + self.__nombre + "\nDNI: " + str(self.__dni) + "\nEdad: " + str(self.__edad) + "\nSexo: " + self.__sexo
        aux = aux + "\nPeso: " + str(self.__peso) + "\nAltura: " + str(self.__altura)
        return aux

    def __generarDNI(self):
        charDni = ["T","R","W","A","G","M","Y","F","P","D","X","N","J","Z","S","Q","V","H","L","C","K","E"]
        num = Random.randrange(10000000,99999999)
        dni = str(num) + charDni[num/23]
        return dni
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setAltura(self,altura):
        self.__altura = altura
    def setEdad(self,edad):
        self.__edad = edad
    def setPeso(self,peso):
        self.__peso = peso
    def setSexo(self,sexo):
        self.__sexo = sexo
"""Programa"""
nombre = input("Introduce el nombre: ")
edad = input("Introduce la edad: ")
sexo = input("Introduce el sexo: ")
peso = input("Introduce el peso: ")
altura = input("Introduce la altura: ")
persona1 = Persona(nombre,edad,peso,altura,sexo)
persona2 = Persona(nombre,edad,0,0,sexo)
persona3 = Persona()
print(persona1.calcularMC())
