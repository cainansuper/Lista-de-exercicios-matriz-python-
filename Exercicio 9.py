tamLinhas = int(input("Digite o número de linhas: "))
matriz = [0] * tamLinhas
tamColunas = int(input("Digite o número de colunas: "))
for i in range(len(matriz)):
    matriz[i] = [0] * tamColunas
    for l in range(len(matriz[i])):
        matriz[i][l] = int(input("Digite um número: "))

soma = 0

for i in range(0, 6):
    linha = int(input("Digite a linha da coordenada a ser escolhida: "))
    coluna = int(input("Digite a coluna da coordenada a ser escolhida: "))
    soma += matriz[linha][coluna]

print(soma)