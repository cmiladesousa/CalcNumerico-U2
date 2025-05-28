import numpy as np
import time
from scipy.io import mmread # Biblioteca para leitura das matrizes dadas pelo professor

inicio = time.time()

Aentrada = mmread ('bcsstk22.mtx')
#Aentrada = mmread ('bcsstk23.mtx')
#Aentrada = mmread ('bcsstk24.mtx')
A = Aentrada.toarray()
# Ordem da matriz A de entrada:

n = A.shape[0]

# Declaração das matrizes B, X, Y e C:

B = np.random.randint(1, 51, size = n) # Gera vetor B aleatório com números de 1 a 50
X = [0.0 for _ in range(n)]
Y = [0.0 for _ in range(n)] # Matriz para guardar o valor de X anterior para cálculo da dA e dR
C = [0.0 for _ in range(n)] # Valores da distância Absoluta
R = [0.0 for _ in range(n)] # Para cálculo do vetor resíduo

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
    print ('VETOR X:')
    print ()
    print([float(x) for x in X])
    print ()
    print('DISTÂNCIA ABSOLUTA:')
    print()
    print(float(maiorAbs))
    print()
    print('DISTÂNCIA RELATIVA:')
    print()
    print(float(maiorRel))
    print()

# Vetor resíduo:

    for i in range (n):
        somaresiduo = 0
        for j in range (n):
            somaresiduo = (A[i][j] * X[j]) + somaresiduo
        R[i] = B[i] - somaresiduo
    print ('RESÍDUO:')
    print ()
    print([float(r) for r in R])

# Mensagem caso não seja diagonalmente dominante:

else: print('Não é diagonalmente dominante!')

fim = time.time()
tempo = fim - inicio
print ()
print ('TEMPO:')
print (tempo)