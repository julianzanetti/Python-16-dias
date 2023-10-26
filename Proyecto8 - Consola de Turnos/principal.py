import numeros
opcion = 0

def menu():
    print("*" * 50)
    print(f"Bienvenido a Farmacia Python".center(50, " "))
    print("*" * 50)
    print(f"Estas son nuestras Areas:")
    print("   1- Perfumeria.")
    print("   2- Farmacia.")
    print("   3- Cosmeticos.")
    while True:
        try:
            opc = int(input("A que Area desea dirigirse (1-3): "))
            if opc > 3:
                print(f"ERROR! Ingresaste un numero mayor a 4.")
            elif opc < 1:
                print(f"ERROR! Ingresaste un numero menor a 1.")
            else:
                return opc
        except ValueError as e:
            print(e)
            print(f"ERROR! No esta permitido caracteres")


while True:
    opcion = menu()
    if opcion == 1:
        numeros.decorador("P")
    elif opcion == 2:
        numeros.decorador("F")
    elif opcion == 3:
        numeros.decorador("C")
    try:
        otro_turno = input("Desea sacar otro turno? [S] [N]: ").upper()
        ["S", "N"].index(otro_turno)
    except ValueError:
        print("Esa no es una opcion valida")
    else:
        if otro_turno == "N":
            print("Gracias por su visita")
            break