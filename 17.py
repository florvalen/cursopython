n = input ("Ingrese un valor a sumar: ")
if not n.isdigit():
    print ("ERROR, lo ingresado no es numerico")
else:
    resultado = int(n)
    final = True
    while final:
        if  not n == 0:
            n = input("Ingrese otro valor a sumar: ")
            if n.isdigit():
                n = int(n)
                resultado = resultado + n
            else:
                print("ERROR, ingrese valor numerico.")
            print(resultado)
        else:
            final = False
    print (f"La suma total  de los numeros ingresados es: : {resultado} ")