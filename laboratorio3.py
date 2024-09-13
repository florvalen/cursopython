import pyttsx3
from groq import Groq
while True:
    contenido  =input( "A continuacion escribe lo que quieras sabero escribe Q para salir ").capitalize
    if contenido=="Q" or contenido =="SALIR":
        exit  ("Gracias por hablar con nosotros hasta la proxima")
        
    client = Groq(
        api_key="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",
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": contenido, 
            }
        ],
        model="llama3-8b-8192",
    )
    engine=pyttsx3.init()
    engine.say(chat_completion.choise[0].message.content)
    engine.runAndWait()
    print(chat_completion.choise[0].message.content)
