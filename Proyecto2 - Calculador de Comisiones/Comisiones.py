nombre = input("Ingrese su nombre: ")
ventas = float(input("Ingrese las ventas totales del mes: "))
calculo = ventas * 0.13
print(f"Hola {nombre}, tus comisiones en este mes son de {round(calculo, 1)}")
