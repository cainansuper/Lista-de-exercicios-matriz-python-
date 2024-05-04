matriz = [0] * 4
for i in range(len(matriz)):
    matriz[i] = [0] * 4
    for o in range(len(matriz[i])):
        matriz[i][o] = int(input("Digite um número: "))

maior = 0

for i in range(len(matriz)):
    print(matriz[i])
    for o in range(len(matriz[i])):
        if matriz[i][o] > 10:
            maior += 1

print("Existem", maior, "valores maiores que 10! ")