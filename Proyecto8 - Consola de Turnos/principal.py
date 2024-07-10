import os
import numeros

inicio = None

def bienvenida():
    print("="*50)
    print("Bienvenido a la farmacia PYTHON".center(50))
    print("=" * 50)


def menu():
    letras = ["P", "C", "F", "S"]
    while True:
        print("(P) - Perfumeria")
        print("(F) - Farmacia")
        print("(C) - Cosmetico")
        print("(S) - Salir")
        opcion = input("Ingrese una opcion: ").upper()
        if opcion in letras:
            return opcion
        else:
            print("ERROR! Solamente esta permitido la (P), (F) o (C)")


def otro_turno():
    while True:
        opcion = input("Desea sacar otro turno (S)(N): ").upper()
        if not opcion in ["S", "N"]:
            print("ERROR! Solamente esta permitido la (S) o (N)")
        elif opcion == "N":
            return "S"
        else:
            os.system("cls")
            return None


while inicio != "S":
    bienvenida()
    inicio = menu()
    os.system("cls")
    if inicio == "P":
        numeros.decorador("P")
        inicio = otro_turno()
    elif inicio == "F":
        numeros.decorador("F")
        inicio = otro_turno()
    elif inicio == "C":
        numeros.decorador("C")
        inicio = otro_turno()
else:
    os.system("cls")
    print("Gracias por utilizar el banco PYTHON!")
