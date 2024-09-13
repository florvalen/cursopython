#funcion para validar un texto
def validar_texto():
    while True:
        texto = input ("Ingrese un texto: ")
        if not texto.isdigit():
            break
        else:
            print ("Ingrese un texto valido")
                
    return texto

texto_imprimir = validar_texto()
print(f"El texto ingresado es: {texto_imprimir}")