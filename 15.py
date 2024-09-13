contador = 0
seguir = True
while seguir:
    valor = input ("ingrese un valor numerico o F para salir: ")
    contador += 1
    valor = valor.upper()
    if contador == 3 or valor == "F":
        seguir = False
        print (f"La rueda se ejecuto correctamente {contador} veces.")