class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, nro_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.nro_cuenta = nro_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.nro_cuenta}: {self.balance}"

    def depositar(self, deposito):
        self.balance += deposito
        print(f"¡Ingreso exitoso!")

    def retirar(self, retiro):
        if self.balance == 0:
            print(f"Tienes que depositar primero.")
        elif self.balance >= retiro:
            self.balance -= retiro
            print(f"¡Retiro exitoso!")
        else:
            print(f"Fondos Insuficiente")


def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nro_cuenta = int(input("Ingrese su numero de cuenta: "))
    cliente = Cliente(nombre, apellido, nro_cuenta)
    return cliente


def menu():
    print(f"Cuenta Bancaria".center(50, "-"))
    print("1- Depositar")
    print("2- Retirar")
    print("3- Salir")
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion > 3:
                print(f"ERROR! Ingresaste un numero mayor a 3.")
            elif opcion < 1:
                print(f"ERROR! Ingresaste un numero menor a 1.")
            else:
                return opcion
        except ValueError as e:
            print(e)
            print(f"ERROR! No esta permitido caracteres")


opcion = 0
cliente = crear_cliente()
while opcion != 3:
    print("*" * 50)
    print(cliente)
    print("*" * 50)
    print("")
    opcion = menu()
    if opcion == 1:
        monto_dep = int(input("Monto a depositar: "))
        cliente.depositar(monto_dep)
    elif opcion == 2:
        monto_ret = int(input("Monto a retirar: "))
        cliente.retirar(monto_ret)
else:
    print("*" * 50)
    print(cliente)
    print("*" * 50)
    print(f"Gracias por operar en nuestro banco")