n1 = input ("Ingrese un numero para obtener su tabla de multiplicacion: ")
if n1.isdigit():
    n1 = int(n1)
    n2 = 1
    while  n2 <= 10:
        resultado = n1 * n2
        print (f"{n1} x {n2} = {resultado}")
        n2 += 1
else:
    print ("ERROR, lo ingresado no corresponde a numero")
exit()