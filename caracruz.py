import random
while True:
    numero_aleatorio = random.randint(1,3)

    if numero_aleatorio == 1:
        eleccion_PC = "CARA"
    elif numero_aleatorio == 2:
        eleccion_PC = "CRUZ"
    elif numero_aleatorio == 3:
        eleccion_PC = "CANTO"
    
eleccion_usuario = input("seleccione CARA(1) o CRUZ(2) para jugar o (T)para terminar el juego:")

eleccion_usuario = eleccion_usuario.upper()



if eleccion_usuario == 1 or eleccion_usuario