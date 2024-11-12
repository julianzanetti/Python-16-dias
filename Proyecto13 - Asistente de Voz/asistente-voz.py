import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import wikipedia
import datetime

# Escuchar el audio y devolverlo en texto
def transformar_audio_texto():

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


# Informar que hora es
def pedir_hora():

    # Crear una variable con los datos de la hora
    hora = datetime.datetime.now()
    print(hora)

    # Decir la hora
    hablar(f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos")


def saludo_inicial():

    # Variable para la hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buenos dias"
    else:
        momento = "Buenas tardes"

    # Decir el saludo
    hablar(f"{momento}, soy Florencia, tu asistente personal. Por favor, dime en que te puedo ayudar")


def pedir_cosas():

    #Activar saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    #loop central
    while comenzar:
        #Activar el micro y guardar el pedido en un string
        pedido = transformar_audio_texto().lower()

        if "abrir youtube" in pedido:
            hablar(f"Con gusto, estoy abriendo YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "abrir el navegador" in pedido:
            hablar("Claro, estoy en eso")
            webbrowser.open("https://www.google.com")

        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue

        elif "qué hora es" in pedido:
            pedir_hora()
            continue

        elif "buscar en wikipedia" in pedido:
            hablar("Buscando eso en wikipedia")
            pedido = pedido.replace("buscar en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(f"En wikipedia dice lo siguiente:")
            hablar(resultado)
            continue


pedir_cosas()
