somaImpares = 0
somaColuna0 = 0
somaColuna1 = 0
somaColuna2 = 0
somaLinha0 = 0
somaLinha1 = 0
somaLinha2 = 0

matriz = [0] * 3
for i in range(len(matriz)):
    matriz[i] = [0] * 3
    for l in range(len(matriz[i])):
        matriz[i][l] = int(input("digite um número: "))
        if (matriz[i][l] % 2) == 1:
            somaImpares += matriz[i][l]
        if i == 0:
            somaLinha0 += matriz[i][l]
        if i == 1:
            somaLinha1 += matriz[i][l]
        if i == 2:
            somaLinha2 += matriz[i][l]
        if l == 0:
            somaColuna0 += matriz[i][l]
        if l == 1:
            somaColuna1 += matriz[i][l]
        if l == 2:
            somaColuna2 += matriz[i][l]

print("Matriz: ")
for i in range(len(matriz)):
    print(matriz[i])

print("Soma dos números ìmpares: ", somaImpares)
print("Soma da Linha 0: ", somaLinha0)
print("Soma da Linha 1: ", somaLinha1)
print("Soma da Linha 2: ", somaLinha2)
print("Soma da coluna 0: ", somaColuna0)
print("Soma da coluna 1: ", somaColuna1)
print("Soma da coluna 2: ", somaColuna2)