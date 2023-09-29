from random import randint
nombre = input("Ingrese su nombre: ")
numero = randint(1,101)
intentos = 8
c = 0
print(f"Hola {nombre}, he pensado un numero del 1 al 100, y tienes solamente 8 intentos para adivinar cual es el numero.")
while intentos > 0:
    try:
        num_elegido = int(input("Ingresa el numero que crees que estoy pensando: "))
        if num_elegido > 100 or num_elegido < 1:
            print("Has elegido un numero que no esta permitdo.")
            print("Recuerda que es entre el 1 al 100 inclusive.")
        elif num_elegido < numero:
            print("Tu respuesta es incorrecta.")
            print("Has elegido un numero menor al numero que estoy pensando.")
        elif num_elegido > numero:
            print("Tu respuesta es incorrecta.")
            print("Has elegido un numero mayor al numero que estoy pensando.")
            print("")
        else:
            print("WINNER")
            print(f"{numero} era mi numero secreto, te llevo {c} intentos encontrarlo.")
            break
        c += 1
        intentos -= 1
        print(f"Te quedan {intentos} intentos todavia.")
        print("")
    except ValueError as e:
        print(e)
        print(f"Ingresaste un valor que no es entero. Por favor vuelve a intentarlo.")
        print("")
else:
    print("GAME OVER")
    print(f"Mi numero secreto era el {numero}")