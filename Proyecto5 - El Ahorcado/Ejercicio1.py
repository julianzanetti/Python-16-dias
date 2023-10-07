def devolver_funcion(num1, num2, num3):
    menor, medio, mayor = sorted([num1, num2, num3])
    suma = num1 + num2 + num3
    if suma > 15:
        return f"La suma es {suma}, el numero mayor es {mayor}"
    elif suma < 10:
        return f"La suma es {suma}, el numero menor es {menor}"
    else:
        return f"La suma es {suma}, el numero medio es {medio}"

print(devolver_funcion(0,1,2))