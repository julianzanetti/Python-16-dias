def turno_perfumeria():
    for x in range(1, 10000):
        yield f"P - {x}"


def turno_farmacia():
    for x in range(1, 10000):
        yield f"F - {x}"


def turno_cosmetico():
    for x in range(1, 10000):
        yield f"C - {x}"


p = turno_perfumeria()
f = turno_farmacia()
c = turno_cosmetico()


def decorador(rubro):
    print("-" * 25)
    print("Su numero de turno es:")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y sera atendido")
    print("-" * 25)
    print("\n")
