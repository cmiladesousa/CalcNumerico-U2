import numpy as np
from scipy.io import mmread
import random
import time

################################################## AUXILIARES ##################################################
def criar_matrizIdentidade(tamanho):
    """
    Esta função cria uma matriz identidade usada para criar a matriz L da fatoração LU. Retorna uma matriz criada.

    :param tamanho: o tamanho da matriz
    :type tamanho: int
    :return: numpy.ndarray matriz
    """
    matriz = np.zeros((tamanho, tamanho), dtype=float)
    for i in range(tamanho):
        matriz[i, i] = 1
    return matriz

def pivotamento_parcial(k, pivo, posicao_pivo, P, A, L, n):
    """
    Esta função calcula o pivotamento parcial da matriz A

    :param k: índice na coluna da matriz
    :type k: int
    :param pivo: valor do elemento da matriz A escolhido
    :type pivo: numpy.float64
    :param posicao_pivo: índice do pivô
    :type posicao_pivo: int
    :param P: Vetor de permutação
    :type P: numpy.ndarray
    :param A: Matriz que está sendo fatorada
    :type A: numpy.ndarray
    :param L: Matriz que armazena os multiplicadores calculados durante a fatoração
    :type L: numpy.ndarray
    :param n: ordem da matriz A
    :type n: int
    :return: numpy.float64 pivo
    """
    #Procurando a maior entrada da coluna k
    for i in range(k+1,n):
        
        if(abs(A[i][k]) > abs(pivo)):
            pivo = A[i][k]
            posicao_pivo = i

    #Verificando se o pivô é zero:       
    if(pivo == 0):
        print("\nNão é possível continuar pois a matriz é singular. O algoritmo será fechado.")
        exit()

    #Troca de linhas:
    if(posicao_pivo != k):
        aux = P[k]
        P[k] = P[posicao_pivo]
        P[posicao_pivo]= aux
        for j in range(n):
            troca_A = A[k][j]
            A[k][j] = A[posicao_pivo][j]
            A[posicao_pivo][j] = troca_A
        for col in range(k):
            aux = L[k][col]
            L[k][col] = L[posicao_pivo][col]
            L[posicao_pivo][col] = aux
        pivo = A[k][k]
    return pivo

def fatoracao(n, A, etapas, L, P):
    """
    Esta função fatora a matriz A usando pivotamento parcial

    :param n: ordem da matriz A
    :type n: int
    :param A: Matriz que está sendo fatorada
    :type A: numpy.ndarray
    :param etapas: quantidade de iterações
    :type etapas: int
    :param L: Matriz que armazena os multiplicadores calculados durante a fatoração
    :type L: numpy.ndarray
    :param P: Vetor de permutação
    :type P: numpy.ndarray
    """
    #Cálculo por etapas:
    for k in range(etapas):
        #print(f"\nEtapa {k}")
        #Definição inicial do pivô:
        pivo = A[k][k]
        posicao_pivo = k

        #pivotamento_parcial
        pivo_final = pivotamento_parcial(k, pivo, posicao_pivo, P, A, L, n)

        #Fim da escolha do pivo. Início da fatoração:
        for i in range (n):
            if (i > k):
                #Definição do multiplicador de cada linha abaixo do pivô:
                multiplicador = A[i][k] / pivo_final

                #Armazenando os multiplicadores na matriz L:
                L[i][k] = multiplicador
                
                #Atualização da linha i:
                for count in range (n):
                    A[i][count] = A[i][count] - multiplicador * A[k][count]
def calculoY(B_permutado, L, n): 
    """
    Esta função calcula o vetor Y. Retorna o vetor calculado.

    :param B_permutado: vetor B permutado com auxílio do vetor de permutação P
    :type B_permutado: numpy.ndarray
    :param L: Matriz que armazena os multiplicadores calculados durante a fatoração
    :type L: numpy.ndarray
    :param n: tamanho dos vetores B_permutado e Y e a ordem da matriz L
    :type n: int
    :return: numpy.ndarray Y 
    """
    Y = np.zeros(n, dtype=float) 
    Y[0] = B_permutado[0]
    for i in range (1, n):
        Y[i] = B_permutado[i]
        for j in range (i):
            Y[i] = Y[i] - L[i][j]*Y[j]
    return Y

def calculoX(Y, U, n):
    """
    Esta função calcula o vetor X, que representa as soluções do sistema linear. Retorna o vetor calculado.

    :param Y: vetor Y calculado anteriormente
    :type Y: numpy.ndarray
    :param U: Matriz que armazena os valores da matriz A fatorada anteriormente.
    :type U: numpy.ndarray
    :param n: tamanho dos vetores Y e X e a ordem da matriz U
    :type n: int
    :return: numpy.ndarray X 
    """
    X = np.zeros(n, dtype=float)
    X[n-1] = Y[n-1] / U[n-1][n-1]
    for i in range(n-2, -1, -1): 
        soma = 0
        for j in range(i+1, n):
            soma += U[i][j] * X[j]  
        X[i] = (Y[i] - soma) / U[i][i]
    return X

def calcula_residuo(A_copia, B, X):   
    """
    Esta função calcula o vetor resíduo, que representa o erro da solução aproximada de um sistema linear. Retorna o vetor calculado.

    :param A_copia: Matriz A antes da fatoração
    :type A_copia: numpy.ndarray
    :param B: Vetor B
    :type B: numpy.ndarray
    :param X: Vetor X com as soluções aproximadas
    :type X: numpy.ndarray
    :return: numpy.ndarray residuo
    """ 
    residuo = np.dot(A_copia, X) - B
    return residuo

##########################################################################################################################
################################################## MATRIZ A ##################################################
inicio = time.time()
print("\n------------------------------ ENTRADA DE DADOS ----------------------------------")

#Leitura da matriz A através dos arquivos do Matrix Market
#A = np.array(mmread('bcsstk22.mtx').todense())
#A = np.array(mmread('bcsstk23.mtx').todense())
A = np.array(mmread('bcsstk24.mtx').todense())
print("\nMatriz A lida.")

#Criação da matriz cópia de A:
A_copia = A.copy()

################################################## VETOR B ##################################################
#Criação do vetor B com valores aleatórios de 1 a 50:
B = np.random.randint(1, 51, size=A.shape[0])

#Salvando o vetor B num txt:
#Caso arquivo bcsstk22.mtx usado:
#np.savetxt('LU_vetorB_22.txt', B, fmt='%.6f')

#Caso arquivo bcsstk23.mtx usado:
#np.savetxt('LU_vetorB_23.txt', B, fmt='%.6f')

#Caso arquivo bcsstk24.mtx usado:
np.savetxt('LU_vetorB_24.txt', B, fmt='%.6f')
print("\nArquivo txt com valores do vetor B foi criado.")

##################################### MONTANDO A MATRIZ A FATORADA ##########################################
print("\n----------------------- PROCESSANDO A FATORAÇÃO LU... ---------------------------")

#Ordem da matriz A:
n = A.shape[0]

#Criação da matriz L:
L = criar_matrizIdentidade(n)

#Vetor permutação:
P = []
for i in range(n):
    P.append(i)
P = np.array(P)

#A quantidade de etapas da fatoração será n-1:
etapas = n - 1

#Fatoração:
fatoracao(n, A, etapas, L, P)

# Cópia da matriz A fatorada para U:
U = A.copy()

#print("\nEtapas:", etapas)

###################################### CÁLCULO DE Y, A PARTIR DE L*Y = B #######################################

#Permutar B caso as linhas de A tenham sido permutadas:
B_permutado = B[P]

#Criação do Vetor Y:
Y = calculoY(B_permutado,L, n)

###################################### CÁLCULO DE X, A PARTIR DE U*X = Y ######################################
#Criação do Vetor X:
X = calculoX(Y,U, n)

#Salvando o resultado do vetor X calculado num txt:
#Caso arquivo bcsstk22.mtx usado:
#np.savetxt('LU_solucao_aproximada22.txt', X, fmt='%.6f')

#Caso arquivo bcsstk23.mtx usado:
#np.savetxt('LU_solucao_aproximada23.txt', X, fmt='%.6f')

#Caso arquivo bcsstk24.mtx usado:
np.savetxt('LU_solucao_aproximada24.txt', B, fmt='%.6f')

print("\nArquivo com as soluções X criado")

###################################### CÁLCULO DO RESÍDUO ######################################
#Checando o resíduo:
residuo = calcula_residuo(A_copia, B, X)

#Salvando o resultado do vetor resíduo calculado num txt:
#Caso arquivo bcsstk22.mtx usado:
#np.savetxt('LU_vetor_residuo22.txt', X, fmt='%.6f')

#Caso arquivo bcsstk23.mtx usado:
#np.savetxt('LU_vetor_residuo23.txt', X, fmt='%.6f')

#Caso arquivo bcsstk24.mtx usado:
np.savetxt('LU_vetor_residuo24.txt', B, fmt='%.6f')

print("\nArquivo com o vetor resíduo criado")

# Lê os dados do arquivo
#R_lido = np.loadtxt('LU_vetor_residuo22.txt')
#R_lido = np.loadtxt('LU_vetor_residuo23.txt')
R_lido = np.loadtxt('LU_vetor_residuo24.txt')

# Calcula o maior valor em módulo
maior_residuo = np.max(np.abs(R_lido))

print(f"\nO maior resíduo é: {maior_residuo:.6f}")

fim = time.time()
print(f"\nTempo de execução: {fim - inicio:.6f} segundos")