matriz = [0] * 4
for i in range(len(matriz)):
    matriz[i] = [0] * 4
    for l in range(len(matriz[i])):
        matriz[i][l] = i*l

for i in range(len(matriz)):
    print(matriz[i])