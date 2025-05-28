# Ordem da matriz A de entrada:

n = int(input('Qual a ordem da matriz?'))

# Declaração das matrizes A, B, X, Y e C:

A = [[0.0 for _ in range(n)] for _ in range(n)]
B = [0.0 for _ in range(n)]
X = [0.0 for _ in range(n)]
Y = [0.0 for _ in range(n)] # Matriz para guardar o valor de X anterior para cálculo da dA e dR
C = [0.0 for _ in range(n)] # Valores da distância Absoluta
R = [0.0 for _ in range(n)] # Para cálculo do vetor resíduo

# Laços para leitura de entrada de A e B:

for i in range (n):
    for j in range (n):
        A[i][j] = float(input(f'Elemento A[{i}][{j}]: '))
for i in range (n):
    B[i] = float(input(f'Elemento B[{i}]: '))

# Cálculo dos valores de X iniciais:

for i in range (n):
    X[i] = B[i] / A[i][i]

# Declaração das variáveis de dA e dR, com valores iniciais acima do critério de parada:

maiorAbs = 10
maiorRel = 10
cont = 0 # Contador para auxiliar na definição de diagonalmente dominante

# Laço para verificar se é diagonalmente dominante:

for i in range (n):
    somalinha = 0
    somacoluna = 0
    for j in range (n):
        if i != j:
            somalinha = somalinha + A[i][j]
            somacoluna = somacoluna + A[j][i]
            if A[i][i] > somalinha or A[i][i] > somacoluna:
                cont = cont + 1

# Sendo diagonalmente dominante, faz os cálculos dos X's, dA e dR conforme método:

if cont >= n:
    while maiorAbs > 10**-6 and maiorRel > 10**-6:
        for i in range (n):
            soma = 0
            for j in range (n):
                if i != j:
                    soma = soma + (A[i][j]*X[j])
            Y[i] = X[i]
            X[i] = (B[i] - soma) / A[i][i]
            C[i] = X[i] - Y[i]
        maiorAbs = max(abs(numero) for numero in C)
        maiorRel = maiorAbs/max(abs(numero) for numero in Y)  
    print(X)
    print(maiorAbs)
    print(maiorRel)

# Vetor resíduo:

    for i in range (n):
        somaresiduo = 0
        for j in range (n):
            somaresiduo = (A[i][j] * X[j]) + somaresiduo
        R[i] = B[i] - somaresiduo
    print (R)

# Mensagem caso não seja diagonalmente dominante:

else: print('Não é diagonalmente dominante!')