Lista=[]
def existe_codigo(arg1):
    aux = True
    for articulo in Lista:
        for v in articulo.values():
            if v == arg1:
                aux = False
    return aux
def añadirArticulo():
    exit = True
    while(exit == True):
        codigo = str(input("Introduze el codigo (f para salir): "))
        if codigo != "f":
            if existe_codigo(codigo) == True:
                print("Introduce las carateristicas del articulo")
                nombre = str(input("Nombre: "))
                descripcion = str(input("Descripcion: "))
                aux = False
                while aux == false:
                    pr = str(input("Precio: "))
                    if pr.isdigit():
                        precio = int(pr)
                        articulo = {"Codigo": codigo,
                                    "Nombre": nombre,
                                    "Descripicon": descripcion,
                                    "Precio": precio}
                        aux == True
                        Lista.append(articulo)
                    else:
                        print("El precio es incorrecto, vuelve a meter el precio")
            else:
                print("Ese articulo con ese codigo ya existe")
        else:
            exit = False
    print("Volvemos al menu")
def eliminarArticulo():
    exit = True
    while (exit == True):
        eliArt = str(input("Elige el codigo del producto que desea eliminar(f para salir)"))
        if eliArt != "f":
            encuentra = 0
            for e in Lista.copy():
                if e["Codigo"] == eliArt:
                    Lista.remove(e)
                    encuentra += 1
            if encuentra == 0:
                print("No encuentra datos")
            else:
                print("Articulo eliminado")
        else:
            exit = False
def listarArticulo():
    print("Lista-----------------")
    for articulo in Lista:
        for c,v in articulo.items():
            print(str(c) + " = " + str(v))
        print("-----------------")
def buscarArticulo():
    exit = True
    while (exit == True):
        busArt = str(input("Elige el codigo del producto que desea ver(f para salir)"))
        if busArt != "f":
            encuentra = 0
            for articulo in Lista:
                if busArt in articulo.values() :
                    for c, v in articulo.items():
                        print(str(c) + " = " + str(v))
                        encuentra += 1
            if encuentra == 0:
                print("No encuentra datos")
        else:
            exit = False
def modificarArticulo():
    exit = True
    while (exit == True):
        modArt = str(input("Elige el codigo del producto que desea modificar(f para salir)"))
        if modArt != "f":
            for articulo in Lista:
                if modArt in articulo.values():
                    
        else:
            exit == False
def menu():
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