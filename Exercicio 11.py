linha = int(input("Digite a quantidade de linhas da matriz \t"))
coluna = int(input("Digite a quantidade de colunas da matriz \t"))
conta = 0
gabarito = ['A', 'B', 'C', 'D', 'E']
notas = [float] * linha
matriz = ['X'] * linha
for l in range(len(matriz)):
    matriz[l] = ['X'] * coluna

for l in range(len(matriz)):
    print("Gabarito inicial aluno ",l+1,matriz[l])
for l in range(len(matriz)):
    # ler as colunas
    for c in range(len(matriz[l])):
        valor = input("Digite o valor \t").upper()
        matriz[l][c] = valor

print("Gabarito", gabarito)
for l in range(len(matriz)):
    print("Gabarito final do aluno ",l+1,matriz[l])

#calcular pontos
for l in range(len(matriz)):
    # ler as colunas
    conta = 0
    for c in range(len(matriz[l])):
        if matriz[l][c] == gabarito[c]:
            conta = conta +1
    #print(conta)
    notas[l] = conta

for l in range(len(notas)):
    print("Nota final do aluno",l+1,":",notas[l])