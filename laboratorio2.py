import speech_recognition as sr
r = sr.Recognizer ()
with sr.Microphone() as sourse:
    print("Hable: ")
    audio = r.listen (sourse)
    try:
        text = r.recognize_google(audio, language="es-ES")
        print (f"Dijiste: {text}")
    except sr.UnknownValueError:
        print ("Lo siento, no he podido entenderlo que has dicho")