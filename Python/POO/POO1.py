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
        stn = 0
        peso = 0
        if self.__peso != 0 and self.__altura !=0:
            peso =  self.__peso  / (float(self.__altura)*float(self.__altura))
            if peso <= 17:
                stn = 1
            elif peso >=25.01:
                stn = -1
        else:
            stn = -2
        return stn,peso

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
        rnd = Random()
        num = ""
        for i in range(8):
            num += str(rnd.randint(1,9))
        dni = num + charDni[(int(num)%23)-1]
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
def representarPeso(num):
    aux,imc = num
    stn = ""
    if aux == -2:
        stn = "No se puede calcular el peso ideal"
    elif aux == -1:
        stn = "Tiene muy poco peso"
    elif aux == 0:
        stn = "Esta en su peso ideal"
    elif aux == 1:
        stn = "Tiene sobrepeso"
    return stn
nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo: ")
peso = int(input("Introduce el peso: "))
altura = float(input("Introduce la altura: "))
persona1 = Persona(nombre,edad,peso,altura,sexo)
persona2 = Persona(nombre,edad,sexo)
persona3 = Persona()
print(representarPeso(persona1.calcularMC()))
print(representarPeso(persona2.calcularMC()))
print(representarPeso(persona3.calcularMC()))
print(persona1.esMayorDeEdad())
print(persona2.esMayorDeEdad())
print(persona3.esMayorDeEdad())
print(persona1.toString())
print("----------------------")
print(persona2.toString())
print("----------------------")
print(persona3.toString())
print("----------------------")
