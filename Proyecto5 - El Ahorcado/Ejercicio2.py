def convertidor_palabra(palabra):
    letras_unicas = sorted(set(palabra))
    return letras_unicas

print(convertidor_palabra("entretenido"))