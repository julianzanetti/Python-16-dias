import random
import os


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


class Persona:
    def __init__(self, nombre, apellido):
        self.nom = nombre
        self.ape = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, nro_cta, balance=0):
        super().__init__(nombre, apellido)
        self.nroCta = nro_cta
        self.balance = balance

    def __str__(self):
        return f"""        Nombre: {self.nom}
        Apellido: {self.ape}
        Nro. CtaCte: {self.nroCta}
        Balance de la Cta: {self.balance}"""

    def depositar(self, deposito):
        if deposito > 0:
            self.balance += deposito
            limpiar_pantalla()
        else:
            limpiar_pantalla()
            print("ERROR! No puedes depositar una cantidad negativa o cero.")

    def retirar(self, retiro):
        if retiro > 0:
            if self.balance < retiro:
                limpiar_pantalla()
                print(f"ERROR! No puedes retirar más de lo que posees!")
            else:
                self.balance -= retiro
                limpiar_pantalla()
        else:
            limpiar_pantalla()
            print("ERROR! No puedes retirar una cantidad negativa o cero.")


def bienvenida():
    print("-"*50)
    print("Bienvenido al Banco PYTHON".center(50))
    print("-"*50)


def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numeros_aleatorios = [str(random.randint(0, 9)) for _ in range(8)]
    nro_cuenta = int(''.join(numeros_aleatorios))
    cliente = Cliente(nombre, apellido, nro_cuenta)
    return cliente


def menu(cliente):
    while True:
        print("-" * 50)
        print(cliente)
        print("-" * 50)
        print("1- Depositar")
        print("2- Retirar")
        print("3- Salir")
        try:
            opcion = int(input("Elija una operación: "))
            if opcion not in [1, 2, 3]:
                limpiar_pantalla()
                print("ERROR! Ingresaste una opción no válida.")
            else:
                return opcion
        except ValueError:
            limpiar_pantalla()
            print("ERROR! No está permitido ingresar caracteres no numéricos.")


bienvenida()
cliente = crear_cliente()
limpiar_pantalla()
opcion = 0
while opcion != 3:
    opcion = menu(cliente)
    if opcion == 1:
        try:
            monto_deposito = int(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(monto_deposito)
        except ValueError:
            limpiar_pantalla()
            print("ERROR! Debes ingresar un número.")
    elif opcion == 2:
        try:
            monto_retiro = int(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(monto_retiro)
        except ValueError:
            limpiar_pantalla()
            print("ERROR! Debes ingresar un número.")
else:
    limpiar_pantalla()
    print("Gracias por utilizar el Banco PYTHON!")
