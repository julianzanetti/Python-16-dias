import time
from pathlib import Path
import math
import os
import re
import datetime

ruta = 'Mi_Gran_Directorio'
patron = r'N\D{3}-\d{4}'
hoy = datetime.date.today()
nros_encontrados = []
archivos_encontrados = []
inicio = time.time()


def buscar_numero(archivo):
    mi_archivo = open(archivo, "r")
    texto = mi_archivo.read()
    busqueda = re.search(patron, texto)
    if busqueda:
        return busqueda
    else:
        return None


def crear_lista():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            resultado = buscar_numero(Path(carpeta, arch))
            if resultado != None:
                nros_encontrados.append(resultado.group())
                archivos_encontrados.append(arch.title())


def mostrar():
    indice = 0
    print('-'*30)
    print(f"Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}")
    print('')
    print(f'Archivo\t\t\tNro. Serie')
    print(f"-------\t\t\t----------")
    for arch in archivos_encontrados:
        print(f"{arch}\t{nros_encontrados[indice]}")
        indice +=1
    print("")
    print(f"Numeros encontrados: {len(nros_encontrados)}")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duracion de la busqueda: {math.ceil(duracion)} segundos")


crear_lista()
mostrar()
