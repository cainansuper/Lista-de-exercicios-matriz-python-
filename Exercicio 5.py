x = 0
linha = 0
coluna = 0
validar = 0

matriz = [0] * 5
for i in range(len(matriz)):
    matriz[i] = [0] * 5
    for l in range(len(matriz[i])):
        matriz[i][l] = int(input("Digite um número: "))

x = int(input("Digite um valor: "))

for i in range(len(matriz)):
    for l in range(len(matriz[i])):
        if matriz[i][l] == x:
            validar += 1
            linha = i
            coluna = l

if validar > 0:
    print(x, "encontra-se na linha ", linha, ", coluna ", coluna)
    for i in range(len(matriz)):
        print(matriz[i])
else:
    print("Valor não foi encontrado! ")
    for i in range(len(matriz)):
        print(matriz[i])
