somaDiagonalP = 0
somaColuna0 = 0
somaColuna1 = 0
somaColuna2 = 0
somaLinha0 = 0
somaLinha1 = 0
somaLinha2 = 0

tamLinhas = int(input("Digite o número de linhas: "))
matriz = [0] * tamLinhas
tamColunas = int(input("Digite o número de colunas: "))
for i in range(len(matriz)):
    matriz[i] = [0] * tamColunas
    for l in range(len(matriz[i])):
        matriz[i][l] = int(input("Digite um número: "))
        if i == l:
            somaDiagonalP += matriz[i][l]

for i in range(len(matriz)):
    for l in range(len(matriz[i])):
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
        
if (somaLinha0 and somaLinha1 and somaLinha2 and somaColuna0 and somaColuna1 and somaColuna2) == somaDiagonalP:
    print("A matriz: ")
    for i in range(len(matriz)):
        print(matriz[i])
    print("É um quadrado mágico! ")
else:
    print("A matriz: ")
    for i in range(len(matriz)):
        print(matriz[i])
    print("Não é um quadrado mágico! ")
