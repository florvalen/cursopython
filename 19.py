ingreso = input ("ingrese un numero: ")
import random
azar = random.randint (1,10)
chances = 3
if  ingreso.isdigit :
    ingreso = int(ingreso)
    while chances >= 1 :
        if ingreso == azar:
            print ("felicidades, acertaste!!!!!!")
        else:
            chances -= 1
else:
    print ("Lo siento, no acertaste...")
print (ingreso, azar)
exit()