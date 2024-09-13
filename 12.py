entrada = input ("ingrese testo: ")
if entrada.isalpha() or entrada.isspace():
    print (f"el texto ingresado es {entrada.upper()}")
else:
    print("ERROR: Debe ingresar solo texto (letras o espacios)")

