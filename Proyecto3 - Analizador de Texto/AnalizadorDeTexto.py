texto = input("Ingrese un texto: ")
print("Ahora te vamos a pedir que ingreses 3 letras.")
letras = []
letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())

opcion = None
while opcion != 0:
    print("")
    print("1 - Cuantas veces aparece las palabras que elegiste?")
    print("2 - Quieres saber el total de palabras que contiene el texto?")
    print("3 - Primera y Ultima palabra del texto")
    print("4 - Texto invertido")
    print("5 - La palabra python se encuentra dentro del texto?")
    print("0 - Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print("Cuantas veces aparece las palabras que elegiste?")
        print(f"La letra {letras[0]} aparece {texto.lower().count(letras[0])} veces")
        print(f"La letra {letras[1]} aparece {texto.lower().count(letras[1])} veces")
        print(f"La letra {letras[2]} aparece {texto.lower().count(letras[2])} veces")
    elif opcion == 2:
        print(f"El texto tiene un total de {len(texto)} palabras")
    elif opcion == 3:
        texto2 = list(texto)
        print(f"La primera letra del texto es {texto2[0]} y la ultima palabra es {texto2[-1]}")
    elif opcion == 4:
        print(f"Asi quedaria el texto que ingresaste invertido...")
        texto2 = list(texto)
        texto2.reverse()
        nuevo_texto = "".join(texto2)
        print(nuevo_texto)
    elif opcion == 5:
        print(f"La palabra python se encuentra dentro del texto?")
        buscar_palabra = "python" in texto.lower()
        dic = {True: "Si", False: "No"}
        print(dic[buscar_palabra])
    elif opcion == 0:
        print("Salimos del programa")
    else:
        print("Numero incorrecto...")
        opcion = int(input("Ingrese una opcion: "))