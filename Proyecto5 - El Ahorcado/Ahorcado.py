from random import choice

palabras = choice(["perro", "gato", "elefante", "jirafa", "omnitorrinco", "hipopotamo", "leon", "serpiente", "raton"])
vidas = 6
letras_correctas = []
letras_incorrectas = []

def validar_letra(letra):
    if letra.isalpha() and len(letra) == 1:
        return letra
    elif letra.isdigit():
        print(f"ERROR! No esta permitido ingresar numeros")
    else:
        print(f"ERROR! Ingresaste una cadena de caracteres")

def ingreso_letra():
    while True:
        letra = input("Ingrese una letra: ").lower()
        if validar_letra(letra):
            return letra

def chequear_letra(letra):
    if letra in palabras:
        print("")
        print("-"*50)
        print(f"Muy bien! Ingresaste una letra correcta.")
        letras_correctas.append(letra)
        return True
    else:
        print("")
        print("-"*50)
        print(f"Ups! Ingresaste una letra incorrecta")
        letras_incorrectas.append(letra)
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
while vidas != 0:
    print(f"La palabra oculta es {validacion()}")
    ingreso = ingreso_letra()
    chequeo = chequear_letra(ingreso)
    if chequeo == True:
        print(f"Te quedan {vidas} vidas")
        print("-" * 50)
        print("")
    else:
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
        print("-" * 50)
        print("")
    if validacion() == palabras:
        print("")
        print(f"¡GANASTE!".center(50,"-"))
        print(f"Adivinaste la palabra oculta que era {palabras}")
        break

else:
    print(f"GAME OVER!")
    print(f"La palabra oculta era {palabras}")
