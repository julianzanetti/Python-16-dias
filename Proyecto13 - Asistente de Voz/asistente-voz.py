import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import wikipedia
import datetime

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


transformar_texto_audio()
