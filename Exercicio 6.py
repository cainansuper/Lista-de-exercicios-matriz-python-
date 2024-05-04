matriz1 = [0] * 4
for i in range(len(matriz1)):
    matriz1[i] = [0] * 4
    for l in range(len(matriz1[i])):
        matriz1[i][l] = int(input("Digite um número para a primeira matriz: "))

matriz2 = [0] * 4
for i in range(len(matriz2)):
    matriz2[i] = [0] * 4
    for l in range(len(matriz2[i])):
        matriz2[i][l] = int(input("Digite um número para a segunda matriz: "))

matriz3 = [0] * 4
for i in range(len(matriz3)):
    matriz3[i] = [0] * 4
    for l in range(len(matriz3[i])):
        if matriz1[i][l] >= matriz2[i][l]:
            matriz3[i][l] = matriz1[i][l]
        else:
            matriz3[i][l] = matriz2[i][l]

print("Matriz 1: ")
for i in range(len(matriz1)):
    print(matriz1[i])

print("Matriz 2: ")
for i in range(len(matriz2)):
    print(matriz2[i])

print("Matriz 3: ")
for i in range(len(matriz3)):
    print(matriz3[i])