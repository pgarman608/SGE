Lista=[]
def existe_codigo(arg1):
    aux = True
    for articulo in Lista:
        aux = articulo.get(arg1,False)
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
                precio = int(input("Precio: "))
                articulo = {"Codigo": codigo,
                            "Nombre": nombre,
                            "Descripicon": descripcion,
                            "Precio": precio}
                Lista.append(articulo)
            else:
                print("Ese articulo con ese codigo ya existe")
        else:
            exit = False
    print("Volvemos al menu")
def eliminarArticulo():
    exit = True
    while (exit == True):
        eliArt = str(input("Elige el codigo del producto que desea eliminar"))
        for articulo in Lista:
            if existe_codigo(eliArt):
                exit = articulo.pop(eliArt,False)

def menu():
    print("1 - Dar de alta")
    print("2 - Dar de baja")
    print("3 - Modificar producto")
    print("4 - Buscar producto")
    print("5 - Listar productos")
    print("6 - Salir de la aplicacion")
    aux = int(input("Elegir"))
    return aux

if __name__ == '__main__':
    elegir = 1
    while(elegir != 6):
        elegir = menu()
        if elegir == 1:
            añadirArticulo()
        elif elegir == 2:
            elimnarArticulo()
        elif elegir == 3:
            modificarArticulo()
        elif elegir == 4:
            buscarArticulo()
        elif elegir == 5:
            listarArticulo()
        else:
            print("Adios")
        print("----------------------")