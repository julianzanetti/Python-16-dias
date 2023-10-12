from pathlib import Path
from os import system

opcion = 0
rutas = Path("Recetas")


def bienvenida():
    c = 0
    print("!Bienvenido al Recetario!")
    print(f"La ruta de acceso al directorio donde se encuentra las Recetas es la siguiente: {Path.home() / rutas}")
    for txt in rutas.glob("**/*.txt"):
        c += 1
    print(f"En total tienes {c} recetas")


def menu():
    print(f"Recetario".center(50, "*"))
    print("1- Leer Receta")
    print("2- Crear Receta")
    print("3- Crear Categoria")
    print("4- Elimnar Receta")
    print("5- Eliminar Categoria")
    print("6- Salir")
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion > 6:
                print(f"ERROR! Ingresaste un numero mayor a 6.")
            elif opcion < 1:
                print(f"ERROR! Ingresaste un numero menor a 1.")
            else:
                return opcion
        except ValueError as e:
            print(e)
            print(f"ERROR! No esta permitido caracteres")


def categorias():
    c = 0
    for cate in rutas.iterdir():
        c += 1
        print(f"{c}- {cate.stem}")
    print(f"0- Volver al menu principal")
    while True:
        try:
            categoria = int(input(f"Elige una categoria: "))
            if categoria > c:
                print(f"ERROR! Ingresaste un numero mayor a {c}.")
            elif categoria <0:
                print(f"ERROR! Ingresaste un numero menor a 0.")
            elif categoria == 0:
                return categoria
            else:
                c = 0
                for cate in rutas.iterdir():
                    c += 1
                    if categoria == c:
                        ruta = Path(cate)
                        return ruta.stem
        except ValueError as e:
            print(e)
            print(f"ERROR! No esta permitido caracteres")


def leer_receta():
    c = 0
    categoria = categorias()
    system("cls")
    while categoria != 0:
        ruta = Path(rutas, categoria)
        for archivo in ruta.iterdir():
            c += 1
            if archivo.is_file:
                print(f"{c} - {archivo.stem}")
        c = 0
        receta = int(input("Que receta quieres leer? "))
        system("cls")
        for archivo in ruta.iterdir():
            c += 1
            if archivo.is_file and receta == c:
                contenido = open(archivo, "r")
                print("-#" * 50)
                print(contenido.read())
                print("-#" * 50)
                contenido.close()
        break


def crear_receta():
    categoria = categorias()
    system("cls")
    while categoria != 0:
        nom_receta = input("Escribe el nombre de la receta:") + ".txt"
        ruta = Path(rutas, categoria, nom_receta)
        receta = input("Escribe el contenido de la receta: ")
        system("cls")
        archivo = open(ruta, "w")
        archivo.write(receta)
        print(f"Se ha creado y guardado el archivo {nom_receta} en el directorio {ruta}")
        archivo.close()
        break


def eliminar_receta():
    c = 0
    categoria = categorias()
    system("cls")
    while categoria != 0:
        ruta = Path(rutas, categoria)
        for archivo in ruta.iterdir():
            c += 1
            if archivo.is_file:
                print(f"{c} - {archivo.stem}")
        c = 0
        receta = int(input("Que receta quiere eliminar? "))
        system("cls")
        for archivo in ruta.iterdir():
            c += 1
            if archivo.is_file and receta == c:
                archivo.unlink()
                print(f"La receta {archivo.stem} ha sido eliminada")
        break


def crear_categoria():
    nom_categoria = input("Ingrese el nombre de la Categoria: ")
    ruta_categoria = Path(rutas, nom_categoria)
    system("cls")
    if ruta_categoria.exists():
        print(f"La categoria {nom_categoria} ya existe en la ruta {ruta_categoria}")
    else:
        ruta_categoria.mkdir(parents=True)
        print(f"La categoria {nom_categoria} fue creada con exito en la ruta {ruta_categoria}")


def eliminiar_categoria():
    categoria = categorias()
    system("cls")
    ruta = Path(rutas, categoria)
    for archivo in ruta.iterdir():
        try:
            if archivo.is_file():
                print(f"ERROR! No se puede eliminar la categoria porque existen recetas activas.")
            break
        except:
            ruta.rmdir()
            print(f"La categoria {categoria} ha sido eliminada con exito")


bienvenida()
while opcion != 6:
    print("")
    opcion = menu()
    system("cls")
    if opcion == 1:
        leer_receta()
    elif opcion == 2:
        crear_receta()
    elif opcion == 3:
        crear_categoria()
    elif opcion == 4:
        eliminar_receta()
    elif opcion == 5:
        eliminiar_categoria()
else:
    print(f"¡Gracias por utilizar el Recetario!")
