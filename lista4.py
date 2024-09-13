productos = []
productos = input ("Ingrese el listado de productos a comprar: ")
fin = True
ingreso = "S"
while fin:
    if ingreso == "S" :
        agregar = input ("ingrese producto: ")
        productos.append("agregar")
        ingreso = input("Desea seguir ingresando productos S/N:")
    else:
        fin = False
print (productos)