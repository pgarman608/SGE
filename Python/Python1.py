#Actividad hecha por Pablo García Manzano de 2ºDAM
#Crearemos una lista para guardar los articulos que seran diccionarios
Lista=[]
#Crearemos un metodo para comprobar si existe el articulo
def existe_codigo(arg1):
    #Crearemos una variable booleana que nos saque si existe o no el codigo del articulo en la lista
    aux = True
    #Dos bucles: Uno para recorer los diccionarios y otro para los valores de cada diccionario
    for articulo in Lista:
        for v in articulo.values():
            #Si el valor es igual al arg1 nos pondra un false
            if v == arg1:
                aux = False
    #Sacaremos el variable booleana
    return aux
def añadirArticulo():
    #Tendremos que tener un bolean para salir del bucle que tenedremos en todo el metodo
    exit = True
    while(exit == True):
        #Preguntaremos el codigo del producto que querramos meter
        codigo = str(input("Introduze el codigo (f para salir): "))
        #Si es f saldremos del bucle
        if codigo != "f":
            #Con el metodo anterior preguntaremos si no existe el codigo
            if existe_codigo(codigo) == True:
                print("Introduce las carateristicas del articulo")
                #Añadiremos el metodo para añadir el articulo
                addArticulo(codigo)
            else:
                #Si el codigo existe
                print("Ese articulo con ese codigo ya existe")
        else:
            exit = False
    print("Volvemos al menu")
#Metodo para eliminar el articulo
def eliminarArticulo():
    # Tendremos que tener un bolean para salir del bucle que tenedremos en todo el metodo
    exit = True
    while (exit == True):
        # Preguntaremos el codigo del producto que querramos borrar
        eliArt = str(input("Elige el codigo del producto que desea eliminar(f para salir)"))
        # Si es f saldremos del bucle
        if eliArt != "f":
            # Con el metodo anterior preguntaremos si existe el codigo
            if existe_codigo(eliArt) == False:
                #Con un for recorreremos la lista
                for e in Lista:
                    #Comprobaremos que codigo tiene cada diciconario y si es el que ha introducido
                    if e["Codigo"] == eliArt:
                        #Eliminaremos el articulo de la lista
                        Lista.remove(e)
                        print("Articulo eliminado")
            else:
                print("No encuentra datos")
        else:
            exit = False
def listarArticulo():
    print("Lista-----------------")
    #Tendremos dos for: Uno para recorrer los articulos de la lista y otro para la informacion de los
    #Articulos
    for articulo in Lista:
        for c,v in articulo.items():
            #Lo representaremos en pantalla
            print(str(c) + " = " + str(v))
        print("-----------------")
def buscarArticulo():
    # Tendremos que tener un bolean para salir del bucle que tenedremos en todo el metodo
    exit = True
    while (exit == True):
        # Preguntaremos el codigo del producto que querramos modificar
        busArt = str(input("Elige el codigo del producto que desea ver(f para salir)"))
        # Si es f saldremos del bucle
        if busArt != "f":
            # Con el metodo anterior preguntaremos si existe el codigo
            if existe_codigo(busArt) == False:
                #Guardaremos los articulos del array
                for articulo in Lista:
                    #Comprobaremos si el codigo esta en ese articulo
                    if busArt in articulo.values():
                        #Sacaremos todos los articulos por pantalla
                        for c, v in articulo.items():
                            print(str(c) + " = " + str(v))
            else:
                print("No encuentra datos")
        else:
            exit = False
def modificarArticulo():
    # Tendremos que tener un bolean para salir del bucle que tenedremos en todo el metodo
    exit = True
    while (exit == True):
        # Preguntaremos el codigo del producto que querramos modificar
        modArt = str(input("Elige el codigo del producto que desea modificar(f para salir)"))
        # Si es f saldremos del bucle
        if modArt == "f":
            exit = False
        else:
            # Con el metodo anterior preguntaremos si existe el codigo
            if existe_codigo(modArt) == False:
                #haremos un bucle para guardar los articulos
                for e in Lista.copy():
                    #Comprobaremos el codigo introducido por el
                    if e["Codigo"] == modArt:
                        print("Introduce el nuevo nombre, descripcion y precio")
                        #Eliminamos el articulo
                        Lista.remove(e)
                        #Creamos otro con el mismo codigo
                        addArticulo(modArt)
            else:
                print("No existe ningun articulo con ese codigo ")

def addArticulo(arg1):
    #Escribiremos el nombre del articulo
    nombre = str(input("Nombre: "))
    #Escribimos la descripcion del articulo
    descripcion = str(input("Descripcion: "))
    aux = False
    #Crearemos un bucle para el numero, es decir, que no meta un numero en vez de un texto
    while aux == False:
        #Guardaremos el numero pero en string
        pr = str(input("Precio: "))
        #Comprobaremos el si se puede pasar a digito o no
        if pr.isdigit():
            #Si se puede pasar a digito, lo pasaremos a un int
            precio = int(pr)
            #Crearemos el articulo
            articulo = {"Codigo": arg1,
                        "Nombre": nombre,
                        "Descripicon": descripcion,
                        "Precio": precio}
            #Saldremos del bucle poniendo la variable voleana en true
            aux = True
            #Guardaremos el articulo en la lista
            Lista.append(articulo)
        else:
            print("El precio es incorrecto, vuelve a meter el precio")

def menu():
    #Menu principal que hacer con la lista de articulos
    print("1 - Dar de alta")
    print("2 - Dar de baja")
    print("3 - Modificar producto")
    print("4 - Buscar producto")
    print("5 - Listar productos")
    print("6 - Salir de la aplicacion")
    aux = int(input("Elegir: "))
    return aux

if __name__ == '__main__':
    elegir = 1
    while(elegir != 6):
        elegir = menu()
        if elegir == 1:
            añadirArticulo()
        elif elegir == 2:
            eliminarArticulo()
        elif elegir == 3:
            modificarArticulo()
        elif elegir == 4:
            buscarArticulo()
        elif elegir == 5:
            listarArticulo()
        elif elegir == 6:
            print("Adios")
        else:
            print("Introduce un numero correcto")
        print("----------------------")