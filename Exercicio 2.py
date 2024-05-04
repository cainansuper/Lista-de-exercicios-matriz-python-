matriz = [0] * 5
for i in range(len(matriz)):
    matriz[i] = [0] * 5
    for l in range(len(matriz[i])):
        if i == l:
            matriz[i][l] = 1
        else:
            matriz[i][l] = 0

for i in range(len(matriz)):
    print(matriz[i])