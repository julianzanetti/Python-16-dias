from random import choice

palabras = choice(["perro", "gato", "elefante", "jirafa", "omnitorrinco", "hipopotamo", "leon", "serpiente", "raton"])
vidas = 6
letras_correctas = []
letras_incorrectas = []
def ocultar_palabra(palabra):
        palabra_oculta = palabra[0] + ("*" * (len(palabra) - 1))
        return palabra_oculta

def validar_letra(letra):
    if letra.isalpha() and len(letra) == 1:
        return letra
    elif letra.isdigit():
        print(f"ERROR! No esta permitido numeros.")
    else:
        print(f"ERROR! Ingresaste una cadena de caracteres")

def ingreso_letra():
    while True:
        letra = input("Ingrese una letra: ").lower()
        if validar_letra(letra):
            return letra

def chequear_letra(letra_mostrar):
    for indice in range(1, len(palabras)):
        if palabras[indice] == letra_mostrar:
            return True
        else:
            pass
    return False

def validacion():
    palabra_incompleta = palabras[0]
    for letra in palabras[1:]:
        if letra in letras_correctas:
            palabra_incompleta += letra
        else:
            palabra_incompleta += "*"
    return palabra_incompleta

print(f"¡Bienvenido al ahorcado!".center(50, "-"))
print(f"Tienes {vidas} vidas para intentar adivinar la palabra oculta")
print(f"La palabra oculta es: {ocultar_palabra(palabras)}")
while vidas >0:
    ingreso = ingreso_letra()
    chequeo = chequear_letra(ingreso)
    if chequeo == True:
        print("\n-----------------------------------------------------------------------")
        print(f"Muy bien!. Ingresaste una letra correcta.")
        letras_correctas.append(ingreso)
    else:
        print("\n-----------------------------------------------------------------------")
        print(f"Ups!. Ingresaste una letra incorrecta")
        letras_incorrectas.append(ingreso)
        vidas -= 1
    if validacion() == palabras:
        print("")
        print(f"¡GANASTE!".center(50,"-"))
        print(f"La palabra completa es: {palabras}")
        break
    else:
        print(f"Te quedan {vidas} vidas restantes.")
        print(f"Hasta ahora ingresaste estas letras incorrectamente: {letras_incorrectas}")
        print("--------------------------------------------------------------------------\n")
        print(validacion())
else:
    print(f"PERDISTE".center(50, "-"))
    print(f"La palabra completa era: {palabras}")