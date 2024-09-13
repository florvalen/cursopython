import pyttsx3
engine = pyttsx3.init()
engine.say ("Hola, mundo")
#engine.runAndWait()
hablar = input ("Escribilo quequierasque diga: ")
rate = engine.getProperty("rate")
print (f"Lavelocidad es: {rate}")
engine.setProperty("rate",200)
engine.say(hablar)
