import numpy as np
import time

################################################## AUXILIARES ##################################################
def exibir_matriz(matriz, nome):
    """
    Esta função exibe os dados de uma matriz qualquer com 6 casas decimais de precisão.

    :param matriz: uma matriz qualquer
    :type matriz: numpy.ndarray
    :param nome: nome da matriz  
    :type nome: str
    """
    print("\nA Matriz", nome, "é:")
    for linha in matriz:
        print("[", end=" ")
        for valor in linha:
            if abs(valor) < 1e-10:
                valor = 0.0
            print("{:.6f}".format(valor), end=" ")
        print("]")

def exibir_vetor(vetor, nome):
    """
    Esta função exibe os dados de um vetor qualquer com 6 casas decimais de precisão.

    :param vetor: um vetor qualquer
    :type vetor:  ndarray
    :param nome: nome do vetor  
    :type nome: str
    """
    print("\nO vetor", nome, "é:")
    for valor in vetor:
        if abs(valor) < 1e-10:
            valor = 0.0
        print("[ {:.6f} ]".format(valor))

def ler_matriz(tamanho):
    """
    Esta função lê as entradas de uma matriz e armazena seus valores nas devidas posições. Retorna a matriz com valores lidos.

    :param tamanho: a ordem da matriz NxN
    :type tamanho: int
    :return: numpy.ndarray matriz
    """
    matriz = np.zeros((tamanho, tamanho), dtype=float)
    for i in range(tamanho):
        for j in range(tamanho):
            matriz[i, j] = float(input(f"Elemento [{i}][{j}]: "))
    return matriz

def ler_vetor(tamanho):
    """
    Esta função lê as entradas de um vetor e armazena seus valores nas devidas posições. Retorna um vetor com os valores lidos.

    :param tamanho: o tamanho do vetor
    :type tamanho: int
    :return: numpy.ndarray vetor
    """
    vetor = np.zeros(tamanho, dtype=float)
    for i in range(tamanho):
        vetor[i] = float(input(f"Elemento [{i}]: "))
    return vetor

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

def calcula_determinante(matriz):
    """
    Esta função calcula o determinante de uma matriz e retorna o valor do determinante calculado.

    :param matriz: matriz alvo
    :type matriz: numpy.ndarray
    :return: float det_
    """
    det_ = float(np.linalg.det(matriz))
    return det_

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
        print("\nEtapa:", k+1)
        
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

        #Exibição da Matriz A fatorada na etapa k:
        print("\nA matriz A fatorada na etapa", k+1, "será:")
        exibir_matriz(A, "A")

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

def exibe_residuo(residuo):
    """
    Esta função os dados do vetor resíduo.

    :param residuo: vetor resíduo.
    :type residuo: numpy.ndarray
    """ 
    print("\nResíduo (Ax - B):")
    for valor in residuo:
        if abs(valor) < 1e-10:
            valor = 0.0
        print("[ {:.6f} ]".format(valor))
##########################################################################################################################
################################################## MATRIZ A ##################################################
inicio = time.time()
print("\n------------------------------ ENTRADA DE DADOS ----------------------------------")

n = int (input("\nDigite a ordem da matriz A: ")) #n é a ordem da matriz A

#Leitura e exibição da matriz A:
print("\nDigite os valores da matriz A, um por um: ")
A = ler_matriz (n)
exibir_matriz(A, "A")

#Criação da matriz cópia de A:
A_copia = A.copy()

#Só prossegue se determinante não for zero:
determinante = calcula_determinante(A)
if np.isclose(determinante, 0):
    print("\nA matriz é singular (não possui inversa), ou seja, seu determinante é zero e, por isso, a fatoração LU não pôde continuar. Logo, o sistema linear ou não possui soluções ou possui infinitas soluções. Portanto, o algoritmo será encerrado.")
else:
    print("\nComo o determinante da matriz A é diferente de zero, o sistema linear possui uma única solução. Assim, podemos prosseguir com a fatoração LU!")

    ################################################## VETOR B ##################################################
    #Leitura e exibição do vetor B:
    print("\nDigite os valores do vetor B, um por um: ")
    B = ler_vetor(n)
    exibir_vetor(B, "B")

    ##################################### MONTANDO A MATRIZ A FATORADA ##########################################
    print("\n----------------------- PROCESSANDO A FATORAÇÃO LU... ---------------------------")

    #Criação da matriz L:
    L = criar_matrizIdentidade(n)

    #Vetor permutação:
    P = []
    for i in range(n):
        P.append(i)
    P = np.array(P)

    #A quantidade de etapas da fatoração será n-1:
    etapas = n - 1
    print("\nTeremos", etapas, "etapa(s).")
   
    #Fatoração:
    fatoracao(n, A, etapas, L, P)

    # Cópia da matriz A fatorada para U:
    U = A.copy()

    #Exibir L e U:
    exibir_matriz(L,"L")
    exibir_matriz(U, "U")

    ###################################### CÁLCULO DE Y, A PARTIR DE L*Y = B #######################################
    #Permutar B caso as linhas de A tenham sido permutadas:
    B_permutado = B[P]

    #Criação do Vetor Y:
    Y = calculoY(B_permutado,L, n)

    #Exibição do vetor Y calculado:
    exibir_vetor(Y,"Y")

    ###################################### CÁLCULO DE X, A PARTIR DE U*X = Y ######################################
    #Criação do Vetor X:
    X = calculoX(Y,U, n)

    #Exibição do vetor X calculado:
    exibir_vetor(X,"X")

    ###################################### CÁLCULO DO RESÍDUO ######################################
    #Checando o resíduo:
    residuo = calcula_residuo(A_copia, B, X)
    exibe_residuo(residuo)

fim = time.time()
print(f"\nTempo de execução: {fim - inicio:.6f} segundos")