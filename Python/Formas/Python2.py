class Empleado():
    multiplicador = 1
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
        aux = "Nombre: " + self.nombre + "\nApellidos :" + self.apellido1 + " " + self.apellido2
        aux = aux + "\nDNI: " + self.dni + "\nDireccion: " + str(self.direccion) + "\nTelefono: " + str(self.telefono)
        aux = aux + "\nSalario: " + self.salario + "\nSupervisor: " + self.supervisor

    def setSupervisor(self,supervisor=""):
        self.supervisor = supervisor

    def incrementarSalario(self):
        self.salario *= self.multiplicador

class Secretario(Empleado):
    def __init__(self, nombre="", apellido1="", apellido2="", dni="", direccion="", telefono=0, salario=1, supervisor=Empleado()
    ,despacho="",fax=0):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, telefono, salario, supervisor)
        self.despacho = despacho
        self.fax = fax
        self.multiplicador = 1.05

    def toString(self):
        return "Secrectario/a: \n" + super().toString() + "\nDespacho: " + self.despacho +"\nFax: " + str(self.fax)

class Coche():
    def __init__(self,matricula="", marca="", modelo=""):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

class Vendedor(Empleado):
    def __init__(self, nombre="", apellido1="", apellido2="", dni="", direccion="", telefono=0, salario=1, supervisor=Empleado(),
    coche=Coche(),telefonoMovil=0,areaTrabajo="",listaClientes=list(),porcentajeVentas=0):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, telefono, salario, supervisor)
        self.multiplicador = 1.10
        self.coche = coche
        self.telefonoMovil = telefonoMovil
        self.areaTrabajo = areaTrabajo
        self.listaClientes = listaClientes
        self.porcentajeVentas= porcentajeVentas

    def cambiarCoche(self,coche=Coche()):
        self.coche = coche

    def altaCliente(self,cliente=""):
        self.listaClientes.append(cliente)

    def bajaCliente(self,cliente=""):
        self.listaClientes.remove(cliente)

    def toString(self):
        aux = "Vendedor: \n" + super().toString() + "\nCoche" + self.coche.matricula + "\nTelefono Movil: " + str(self.telefonoMovil)
        aux = aux + "\nArea de trabajo: " + self.areaTrabajo + "\nLista de clientes: " + self.listaClientes
        aux = aux + + "\nPorecentaje de las ventas: " + str(self.porcentajeVentas)
        return aux

class JefeZona(Empleado):
    def __init__(self, nombre="", apellido1="", apellido2="", dni="", direccion="", telefono=0, salario=1, supervisor="",
    secretario=Secretario(),despacho="",listaVendedores=list(),coche=Coche()):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, telefono, salario, supervisor)
        self.multiplicador = 1.20
        self.secretario = secretario
        self.despacho=despacho
        self.listaVendedores = listaVendedores
        self.coche = coche

    def toString(self):
        aux = "Jefe de Zona: \n" + super().toString() + "\nSecretario: " + self.secretario.dni + "\nDespacho: " + self.despacho
        aux = aux + "\nLista de Vendedores" + self.listaVendedores + "\nCoche: " + self.coche
        return aux

    def setSecretario(self,secretario=Secretario()):
        self.secretario = secretario

    def setCoche(self,coche=Coche()):
        self.coche = coche