import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import wikipedia
import datetime

# Escuchar el audio y devolverlo en texto
def transformar_texto_audio():

    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzo la grabacion
        print("Ya puedes hablar...")

        # Guardar lo que escuche en audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            # Prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # Devolver pedido
            return pedido

        # En caso de que no comprenda el audio.
        except sr.UnknownValueError:
            # Prueba de que no comprendio el audio
            print("Ups, No hay servicio.")

            #Devolver error
            return "Sigo esperando."

        # En caso de que no resuelva el pedido.
        except sr.RequestError:
            # Prueba de que no comprendio el audio
            print("Ups, No entendí.")

            #Devolver error
            return "Sigo esperando."

        # Error inesperado.
        except:
            # Prueba de que no comprendio el audio
            print("Ups, Algo salio mal.")

            #Devolver error
            return "Sigo esperando."


# Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # Encender pyttsx3
    engine = pyttsx3.init()

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar el dia de la semana
def pedir_dia():

    # Crear variable con el dia de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con los nombres de los dias
    calendario = {0: "Lunes",
                  1: "Mares",
                  2: "Miercoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sabado",
                  6: "Domingo"}

    # Decir el dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")

pedir_dia()
