class Empleado():
    multiplicador = 1
    """El init de la clase"""
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
    """Pasaremos todos los metodos como si fuesen un String"""
    def toString(self):
        aux = "Nombre: " + self.nombre + "\nApellidos :" + self.apellido1 + " " + self.apellido2
        aux = aux + "\nDNI: " + self.dni + "\nDireccion: " + str(self.direccion) + "\nTelefono: " + str(self.telefono)
        aux = aux + "\nSalario: " + str(self.salario) + "\nSupervisor: " + self.supervisor
        return aux
    """Setter del supervisor"""
    def setSupervisor(self,supervisor=""):
        self.supervisor = supervisor
    """Incrementaremos el salario del empleado por el multiplicador"""
    def incrementarSalario(self):
        self.salario *= self.multiplicador
class Secretario(Empleado):
    """El init de la clase"""
    def __init__(self, nombre="", apellido1="", apellido2="", dni="", direccion="", telefono=0, salario=1, supervisor=""
    ,despacho="",fax=0):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, telefono, salario, supervisor)
        self.despacho = despacho
        self.fax = fax
        self.multiplicador = 1.05
    """Pasaremos todos los metodos como si fuesen un String"""
    def toString(self):
        return "Secrectario/a: \n" + super().toString() + "\nDespacho: " + self.despacho +"\nFax: " + str(self.fax)

class Coche():
    """El init de la clase"""
    def __init__(self,matricula="", marca="", modelo=""):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

class Vendedor(Empleado):
    """El init de la clase"""
    def __init__(self, nombre="", apellido1="", apellido2="", dni="", direccion="", telefono=0, salario=1, supervisor="",
    coche=Coche(),telefonoMovil=0,areaTrabajo="",listaClientes=list(),porcentajeVentas=0):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, telefono, salario, supervisor)
        self.multiplicador = 1.10
        self.coche = coche
        self.telefonoMovil = telefonoMovil
        self.areaTrabajo = areaTrabajo
        self.listaClientes = listaClientes
        self.porcentajeVentas= porcentajeVentas
    """Setter del coche"""
    def cambiarCoche(self,coche=Coche()):
        self.coche = coche
    """Dar de alta al cliente del vendedor"""
    def altaCliente(self,cliente=""):
        self.listaClientes.append(cliente)
    """Dar de baja al cliente del vendedor"""
    def bajaCliente(self,cliente=""):
        self.listaClientes.remove(cliente)
    """Pasaremos todos los metodos como si fuesen un String"""
    def toString(self):
        aux = "Vendedor: \n" + super().toString() + "\nCoche" + self.coche.matricula + "\nTelefono Movil: " + str(self.telefonoMovil)
        aux = aux + "\nArea de trabajo: " + self.areaTrabajo + "\nLista de clientes: " + self.clientes()
        aux = aux + "\nPorecentaje de las ventas: " + str(self.porcentajeVentas)
        return aux
    """Devolveremos todos los clientes"""
    def clientes(self):
        aux =""
        for cliente in self.listaClientes:
            aux = aux + cliente.nombre +", "
        return aux

class JefeZona(Empleado):
    """El init de la clase"""
    def __init__(self, nombre="", apellido1="", apellido2="", dni="", direccion="", telefono=0, salario=1, supervisor="",
    secretario=Secretario(),despacho="",listaVendedores=list(),coche=Coche()):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, telefono, salario, supervisor)
        self.multiplicador = 1.20
        self.secretario = secretario
        self.despacho=despacho
        self.listaVendedores = listaVendedores
        self.coche = coche
    """Pasaremos todos los metodos como si fuesen un String"""
    def toString(self):
        aux = "Jefe de Zona: \n" + super().toString() + "\nSecretario: " + self.secretario.dni + "\nDespacho: " + self.despacho
        aux = aux + "\nLista de Vendedores: " + self.vendedores() + "\nCoche: " + self.coche.matricula
        return aux
    """Setter del secretario"""
    def setSecretario(self,secretario=Secretario()):
        self.secretario = secretario
    """Setter del coche"""
    def setCoche(self,coche=Coche()):
        self.coche = coche
    """Pasaremos por string todos los vendedores"""
    def vendedores(self):
        aux =""
        for vendedor in self.listaVendedores:
            aux = aux + vendedor.nombre +", "
        return aux
"""Programa de prueba"""
empleado1 = Empleado("Pablo","fernandez","Zamora","1932310O","Calle AB,12",123123123,1400)
secretario1 = Secretario("Antonio","Zamora","Zamora","1928319I","Calle A,1",123123123,1400,empleado1.dni,"Despacho1",323223232)
vendedor1 = Vendedor("Miguel","Ruiz","Moreno","6632310P","Calle C,3",123123123,1400,empleado1.dni,Coche("1234str","Kia","X"),444555666,"Madrid",["Cliente1"],1.03)
jefe1 = JefeZona("Luis","Garcia","alvarez","7775510T","Calle CB,5",123123123,1400,"Sin Supervisor",secretario1,"GranDespacho1",[vendedor1],Coche("3412ttt","kia","A"))
print("---------------------")
print(empleado1.toString())
print(".-.-.")
print(secretario1.toString())
print(".-.-.")
print(vendedor1.toString())
print(".-.-.")
print(jefe1.toString())
print("---------------------")
empleado1.incrementarSalario()
secretario1.incrementarSalario()
vendedor1.incrementarSalario()
jefe1.incrementarSalario()
print("---------------------")
print(empleado1.toString())
print(".-.-.")
print(secretario1.toString())
print(".-.-.")
print(vendedor1.toString())
print(".-.-.")
print(jefe1.toString())
print("---------------------")