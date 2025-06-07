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

# Ordem da matriz A de entrada:
n = int(input('\nQual a ordem da matriz?'))

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

    while maiorAbs > 5*10**-2 and maiorRel > 5*10**-2:
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
    print("\nX =")   
    for valor in X:
        print("[ {:.2f} ]".format(valor))  
    print(f"\n Maior absoluto = {maiorAbs:.2f}")
    print(f"\n Maior rel = {maiorRel:.2f}")
    print(f"\nIterações = {iteracoes}")

    # Vetor resíduo:
    for i in range (n):
        somaresiduo = 0
        for j in range (n):
            somaresiduo = (A[i][j] * X[j]) + somaresiduo
        R[i] = B[i] - somaresiduo
    
    print("\nResiduo =")
    for valor in R:
        print("[ {:.2f} ]".format(valor)) 

fim = time.time()
print(f"\nTempo de execução: {fim - inicio:.2f} segundos")