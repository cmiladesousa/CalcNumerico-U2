import numpy as np
from scipy.io import mmread # Biblioteca para leitura das matrizes dadas pelo professor
import random
import time

#Função que calcula se uma matriz é diagonalmente dominante:
def eh_diagonalmente_dominante(A):
    """
    Esta função verifica se a matriz A é diagonalmente dominante. Retorna true caso seja, e false caso contrário.

    :param A: Matriz A
    :type A: list
    :return: boolean
    """
    n = len(A)
    for i in range(n):
        soma = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) < soma:
            return False
    return True

inicio = time.time()

A = np.array(mmread('bcsstk22.mtx').todense())
#A = np.array(mmread('bcsstk23.mtx').todense())
#A = np.array(mmread('bcsstk24.mtx').todense())
print("\nMatriz A lida.")

# Ordem da matriz A de entrada:

n = A.shape[0]

B = np.random.randint(1, 51, size = n) # Gera vetor B aleatório com números de 1 a 50
#Salvando o vetor B num txt:
#Caso arquivo bcsstk22.mtx usado:
np.savetxt('Seidel_vetorB_22.txt', B, fmt='%.6f')

#Caso arquivo bcsstk23.mtx usado:
#np.savetxt('Seidel_vetorB_23.txt', B, fmt='%.6f')

#Caso arquivo bcsstk24.mtx usado:
#np.savetxt('Seidel_vetorB_24.txt', B, fmt='%.6f')
print("\nArquivo txt com valores do vetor B foi criado.")

X = [0.0 for _ in range(n)]
Y = [0.0 for _ in range(n)] # Matriz para guardar o valor de X anterior para cálculo da dA e dR
C = [0.0 for _ in range(n)] # Valores da distância Absoluta
R = [0.0 for _ in range(n)] # Para cálculo do vetor resíduo

# Sendo diagonalmente dominante, faz os cálculos dos X's, dA e dR conforme método:
if not eh_diagonalmente_dominante(A):
    print("\nA matriz não é diagonalmente dominante. O método pode não convergir ou falhar.")
else:
    # Cálculo dos valores de X iniciais:
    for i in range (n):
        X[i] = B[i] / A[i][i]

    # Declaração das variáveis de dA e dR, com valores iniciais acima do critério de parada:
    maiorAbs = 10
    maiorRel = 10
    iteracoes = 0

    while (maiorAbs > 5*10**-2 and maiorRel > 5*10**-2) or (iteracoes <= 500):
        for i in range (n):
            iteracoes += 1
            soma = 0
            for j in range (n):
                if i != j:
                    soma = soma + (A[i][j]*X[j])
            Y[i] = X[i]
            X[i] = (B[i] - soma) / A[i][i]
            C[i] = X[i] - Y[i]
        maiorAbs = max(abs(numero) for numero in C)
        maiorRel = maiorAbs/max(abs(numero) for numero in Y)
    
    #Salvando o resultado do vetor X calculado num txt:
    #Caso arquivo bcsstk22.mtx usado:
    np.savetxt('Seidel_solucao_aproximada22.txt', X, fmt='%.6f')

    #Caso arquivo bcsstk23.mtx usado:
    #np.savetxt('Seidel_solucao_aproximada23.txt', X, fmt='%.6f')

    #Caso arquivo bcsstk24.mtx usado:
    #np.savetxt('Seidel_solucao_aproximada24.txt', B, fmt='%.6f')

    print("\nArquivo com as soluções X criado")

    # Vetor resíduo:
    for i in range (n):
        somaresiduo = 0
        for j in range (n):
            somaresiduo = (A[i][j] * X[j]) + somaresiduo
        R[i] = B[i] - somaresiduo
    
    #Salvando o resultado do vetor resíduo calculado num txt:
    #Caso arquivo bcsstk22.mtx usado:
    np.savetxt('Seidel_vetor_residuo22.txt', X, fmt='%.6f')

    #Caso arquivo bcsstk23.mtx usado:
    #np.savetxt('Seidel_vetor_residuo23.txt', X, fmt='%.6f')

    #Caso arquivo bcsstk24.mtx usado:
    #np.savetxt('Seidel_vetor_residuo24.txt', B, fmt='%.6f')

    print("\nArquivo com o vetor resíduo criado")

    # Lê os dados do arquivo
    R_lido = np.loadtxt('Seidel_vetor_residuo22.txt')
    #R_lido = np.loadtxt('Seidel_vetor_residuo23.txt')
    #R_lido = np.loadtxt('Seidel_vetor_residuo24.txt')

    # Calcula o maior valor em módulo
    maior_residuo = np.max(np.abs(R_lido))
    print(f"\nO maior resíduo é: {maior_residuo:.6f}")

fim = time.time()
print(f"\nTempo de execução: {fim - inicio:.2f} segundos")