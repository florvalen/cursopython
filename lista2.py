lista_numeros = [48,82,89,23,55]
print (sum(lista_numeros))
print (max(lista_numeros))
print (min(lista_numeros))
lista_numeros = [numero *2 for numero in lista_numeros]
print (lista_numeros)
for numero in lista_numeros:
    if numero %2 == 0:
        print (numero)