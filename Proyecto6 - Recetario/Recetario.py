import os
from pathlib import Path

opcion = 0
ruta_principal = Path("Recetas")

def cant_recetas():
    cant_recetas = 0
    for txt in Path(ruta_principal).glob("**/*.txt"):
        cant_recetas += 1
    print(f"\nActualmente hay {cant_recetas} recetas disponibles para consultar.")


def bienvenida():
    print("*" * 50)
    print("Bienvenido al Recetario".center(50))
    print("*" * 50)
    print("\nLa ruta de acceso al directorio donde se encuentran nuestra carpeta de recetas es:")
    print(Path(os.getcwd(), ruta_principal))
    cant_recetas()


def menu():
    print("1- Leer Receta")
    print("2- Crear Receta")
    print("3- Crear Categoria")
    print("4- Eliminar Receta")
    print("5- Eliminar Categoria")
    print("6- Salir del Programa.")
    while True:
        try:
            opcion = int(input("\nElige una opcion: "))
            if opcion > 6:
                print("ERROR! Ingresaste un numero mayor a 6.")
            elif opcion < 1:
                print("ERROR! Ingresaste un numero menor a 1")
            else:
                return opcion
        except ValueError:
            print("ERROR! No esta permitidos caracteres")


def categoria():
    while True:
        c = 0
        for dir in os.listdir(ruta_principal):
            c += 1
            print(f"{c}- {dir}")
        print(f"{c+1}- Volver al menu de inicio")
        try:
            cat = int(input("Elige una categoria: "))
            if cat > c+1:
                print(f"ERROR! Ingresaste un numero mayor a {c + 1}")
            elif cat < 1:
                print(f"ERROR! Ingresaste un numero menor a 1.")
            elif cat == c+1:
                return None
            else:
                carpeta = 0
                for dir in os.listdir(ruta_principal):
                    carpeta += 1
                    if cat == carpeta:
                        ruta_categoria = Path(ruta_principal, dir)
                        return ruta_categoria
        except ValueError:
            print("ERROR! No esta permitidos caracteres")


def leer_receta():
    os.system("cls "if os.name == "nt" else "clear")
    ruta_categoria = categoria()
    if not ruta_categoria:
        return

    while True:
        c = 0
        for txt in Path(ruta_categoria).glob("*.txt"):
            c += 1
            print(f"{c}- {txt.stem}")

        nro_receta = int(input("Elige una receta a consultar: "))
        if 1 <= nro_receta <= c + 1:
            contador_recetas = 0
            for archivo in ruta_categoria.iterdir():
                contador_recetas += 1
                if archivo.is_file() and contador_recetas == nro_receta:
                    contenido = open(archivo, "r")
                    print(contenido.read())
                    contenido.close()
            break
        else:
            print(f"ERROR! Ingresaste un numero invalido.")


def crear_receta():
    os.system("cls " if os.name == "nt" else "clear")
    ruta_categoria = categoria()
    if not ruta_categoria:
        return

    nom_receta = input("Escribe el nombre de la receta: ")
    ruta_receta = Path(ruta_categoria, f"{nom_receta}.txt")
    receta = input("Escribe la receta: ")
    archivo = open(ruta_receta, 'w')
    archivo.write(receta)
    archivo.close()
    print(f"Receta {nom_receta}.txt creada con exito en la categoria {ruta_receta}")


def crear_categoria():
    c = 0
    for dir in os.listdir(ruta_principal):
        c += 1
        print(f"{c}- {dir}")
    print("")
    while True:
        nueva_cat = input("Ingrese la nueva Categoria: ")
        ruta_cat = Path(ruta_principal, nueva_cat)
        if not ruta_cat.exists():
            ruta_cat.mkdir()
            print(f"La categoria {nueva_cat} ha sido creada con exito!")
            break
        else:
            print(f"ERROR! El directorio {nueva_cat} ya existe!")


def eliminar_receta():
    os.system("cls " if os.name == "nt" else "clear")
    cant_recetas()

    ruta_categoria = categoria()
    if not ruta_categoria:
        return

    while True:
        c = 0
        for txt in Path(ruta_categoria).glob("*.txt"):
            c += 1
            print(f"{c}- {txt.stem}")
        nro_receta = int(input("Elige la receta a eliminar: "))
        if 1 <= nro_receta <= c + 1:
            contador_recetas = 0
            for archivo in ruta_categoria.iterdir():
                contador_recetas += 1
                if archivo.is_file() and contador_recetas == nro_receta:
                    archivo.unlink()
                    print(f"La receta {archivo} ha sido eliminada con exito!")
            break
        else:
            print(f"ERROR! Ingresaste un numero invalido.")


def eliminar_categoria():
    c = 0
    for dir in os.listdir(ruta_principal):
        c += 1
        print(f"{c}- {dir}")
    print(f"{c + 1}- Volver al menu de inicio")
    while True:
        try:
            cat_eliminar = int(input("Ingrese la categoria a eliminar: "))
            if cat_eliminar > c + 1:
                print(f"ERROR! Ingresaste un numero mayor a {c + 1}")
            elif cat_eliminar < 1:
                print(f"ERROR! Ingresaste un numero menor a 1.")
            elif cat_eliminar == c+1:
                return None
            else:
                carpeta = 0
                for dir in os.listdir(ruta_principal):
                    carpeta += 1
                    if cat_eliminar == carpeta:
                        ruta_categoria = Path(ruta_principal, dir)
                        if not any(ruta_categoria.iterdir()):
                            ruta_categoria.rmdir()
                            print(f"Categoria {dir} eliminada con exito!")
                        else:
                            print(f"ERROR! La categoria {dir} contiene recetas dentro.")
                            print(f"Primero elimine las recetas y luego elimine la categoria")
                break
        except ValueError:
            print("ERROR! No esta permitidos caracteres")


bienvenida()
while opcion != 6:
    opcion = menu()
    if opcion == 1:
        leer_receta()
    elif opcion == 2:
        crear_receta()
    elif opcion == 3:
        crear_categoria()
    elif opcion == 4:
        eliminar_receta()
    elif opcion == 5:
        eliminar_categoria()
else:
    print("Gracias por utilizar el recetario!")
