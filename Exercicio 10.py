from random import randint

def bus_valor(matriz, valor):
    res = 0
    for k in range(len(matriz)):
        for c in range(len(matriz[k])):
            if matriz[k][c] == valor:
                res == 1
    return res

matriz = [0] * 5
for l in range(len(matriz)):
    matriz[l] = [0] * 5

for l in range(len(matriz)):
    for o in range(len(matriz[l])):
        valor = randint(0, 99)
        if bus_valor(matriz, valor) == 0:
            matriz[l][o] = valor
        else:
            valor = randint(0, 99)
            while bus_valor(matriz, valor) == 1:
                valor = randint(0, 99)
            matriz[l][o] = valor

for i in range(len(matriz)):
    print(matriz[i])