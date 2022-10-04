Lista=[]
def existe_codigo(arg1):
    aux = True
    for articulo in Lista:
        for i,h in articulo.items():
            if (i == "Codigo") and (h == arg1):
                print("funciona")
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


if __name__ == '__main__':
    añadirArticulo()