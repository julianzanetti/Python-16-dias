def contar_ceros(*args):
    for n in range(len(args) - 1):
        if args[n] == 0 and args[n+1] == 0:
            return True
    return False

print(contar_ceros(5,6,1,0,1,2,0))
print(contar_ceros(5,6,1,0,0,2,0))