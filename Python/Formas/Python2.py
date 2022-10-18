class Empleado():
    def __init__(self,nombre="",apellido1="",apellido2="",dni="",direccion="",telefono=0,salario=1,supervisor=""):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.salario = salario
        self.supervisor = supervisor
        pass
    def toString(self):
        