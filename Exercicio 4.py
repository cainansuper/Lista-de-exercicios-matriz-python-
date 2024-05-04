maior = 0
linha = 0
coluna = 0
matriz = [0] * 4
for i in range(len(matriz)):
    matriz[i] = [0] * 4
    for l in range(len(matriz[i])):
        matriz[i][l] = float(input("Digite um número: "))
        if matriz[i][l] > maior:
            maior = matriz[i][l]
            linha = i
            coluna = l

print()
print("O maior valor é:", maior, "se encontra na linha ", linha, "coluna ", coluna) 
print()

for i in range(len(matriz)):
    print(matriz[i])