import numpy as np
from scipy.io import mmread


def matrizDominante(matriz):
    contador = 0
    n = matriz.shape[0]
    for i in range(n):
        total_linha = sum(abs(matriz[i, j]) for j in range(n) if i != j)
        total_coluna = sum(abs(matriz[j, i]) for j in range(n) if i != j)

        if abs(matriz[i,i]) >= total_linha or abs(matriz[i,i]) >= total_coluna:
            contador += 1
    if contador == n:
        return True
    else:
        print("\n Não convergiu! A matriz não é diagonalmente dominante")
        return False

def residuo(matriz, b, x):
    residuo = np.dot(matriz, x) - b
    print(f"O resíduo máximo foi: {max(abs(residuo))}")

def gauss_jacobi(matriz, b, x, e):
    # Inicialização dos erros
    dis_absoluta = [float('inf')]
    dis_rel = float('inf')
    iteracoes = 0
    n = matriz.shape[0]

    matrizDominante(matriz)
    while (max(abs(np.array(dis_absoluta))) > e or dis_rel > e) and iteracoes < 1000:
        temp = []
        dis_absoluta = []
        for i in range(n):
            if abs(matriz[i, i]) < 1e-12:
                print(f"Divisão por zero: elemento da diagonal matriz[{i},{i}] é zero ou muito próximo de zero.")
                return
            aux = sum(matriz[i, j] * x[j] for j in range(n) if j != i)
            novo_x = (1 / matriz[i, i]) * (b[i] - aux)
            if np.isnan(novo_x) or np.isinf(novo_x):
                print(f"Valor inválido encontrado na iteração {iteracoes}, índice {i}: {novo_x}")
                return
            dis_absoluta.append(novo_x - x[i])
            temp.append(novo_x)

        dis_rel = max(abs(np.array(dis_absoluta))) / max(abs(np.array(temp)))
        x = np.array(temp)
        np.savetxt('jacobi_vetorX.txt', x, fmt='%.6f')
        iteracoes += 1
    
    residuo(matriz, b, x)
    #print(f"Valores de X: {x}")
    print(f"Número de iterações: {iteracoes}")

# Dados de entrada

#Matriz 1
matriz1 = mmread('bcsstk22.mtx')
if not isinstance(matriz1, np.ndarray):
    matriz1 = matriz1.toarray()
b1 = np.random.uniform(1, 50, 138)
np.savetxt('jacobi_vetorB_22.txt',  b1, fmt='%.6f')
x1 = np.zeros_like(b1)

#Matriz 2
matriz2 = mmread('bcsstk23.mtx')
if not isinstance(matriz2, np.ndarray):
    matriz2 = matriz2.toarray()
b2 = np.random.uniform(1, 50, 3134)
np.savetxt('jacobi_vetorB_23.txt', b2, fmt='%.6f')
x2 = np.zeros_like(b2)

#Matriz 3
matriz3 = mmread('bcsstk24.mtx')
if not isinstance(matriz3, np.ndarray):
    matriz3 = matriz3.toarray()
b3 = np.random.uniform(1, 50, 3562)
np.savetxt('jacobi_vetorB_24.txt', b3, fmt='%.6f')
x3 = np.zeros_like(b3)

#Matriz dada em Aula
matriz = np.array([
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
], dtype=float)

b = np.array([7, -8, 6], dtype=float)
x = np.array([0.7, -1.6, 0.6], dtype=float)

#Questão 15 - letra a
matriz15a = np.array([
    [9, 5, 6],
    [2, 3, 1],
    [-1, 1, -3]
], dtype=float)
b15a = np.array([11, 4, -2], dtype=float)
x15a = np.array([11/9, 4/3, -2/-3], dtype=float)

#Questão 15 - letra b
matriz15b = np.array([
    [2, -1, 1],
    [3, 3, 9],
    [3, 3, 5]
], dtype=float)
b15b = np.array([-1, 0, 4], dtype=float)
x15b = np.array([-0.5, 0, 4/5], dtype=float)

#Questão 15 - letra c
matriz15c = np.array([
    [0.252, 0.36, 0.12],
    [0.112, 0.16, 0.24],
    [0.147, 0.21, 0.25]
], dtype=float)
b15c = np.array([7, 8, 9], dtype=float)
x15c = np.array([7/0.252, 8/0.16, 9/0.25], dtype=float)

#Questão 15 - letra d
matriz15d = np.array([
    [3, -2, 5, 1],
    [-6, 4, -8, 1],
    [9, -6, 19, 1],
    [6, -4, -6, 15]
], dtype=float)
b15d = np.array([7, -9, 23, 11], dtype=float)
x15d = np.array([7/3, -9/4, 23/19, 11/15], dtype=float)

#Questão 16 - letra a
matriz16a = np.array([
    [10, -1, 2, 0],
    [-1, 11, -1, 3],
    [2, -1, 10, -1],
    [0, 3, -1, 8]
], dtype=float)
b16a = np.array([6, 25, -11, 15], dtype=float)
x16a = np.array([0.6, 2.2727272727, -1.1, 1.875], dtype=float)

#Questão 16 - letra b
matriz16b = np.array([
    [0, 5, -1, 2],
    [0, 8, -1, 1],
    [2, 1, -1, -1],
    [0, -1, -2, 1]
], dtype=float)
b16b = np.array([6, 25, -11, 15], dtype=float)
x16b = np.array([0, 25/8, 11, 15], dtype=float)

#Questão 16 - letra c
matriz16c = np.array([
    [1, 0.5, -0.1, 0.1],
    [0.2, 1, -0.2, -0.1],
    [-0.1, -0.2, 1, 0.2],
    [0.1, 0.3, 0.2, 1]
], dtype=float)
b16c = np.array([0.2, -2.6, 1, -2.5], dtype=float)
x16c = np.array([0.2, -2.6, 1, -2.5], dtype=float)

#Questão 17 
matriz17 = np.array([
    [1, 1, -1, 2, -1],
    [2, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [4, 0, 0, 16, 0],
    [0, 0, 4, 0, 0]
], dtype=float)
b17 = np.array([2, 2, 2, 20, 4], dtype=float)
x17 = np.zeros_like(b17)

#Questão 18
matriz18 = np.array([
    [1, 2, 1],
    [2, -1, 2],
    [3, 1, 3]
], dtype=float)
b18 = np.array([1, 2, 4], dtype=float)
x18 = np.array([1, -2, 4/3], dtype=float)

#Questão 19
matriz19 = np.array([
    [0, 15, 1, 3],
    [15, 2, 2, 3],
    [0, 4, 15, 1],
    [1, 2, 2, 15]
], dtype=float)
b19 = np.array([-3, 4, 7, 5], dtype=float)
x19 = np.array([0, 2, 7/15, 5/15], dtype=float)

e = 0.001

#print("\n ----------- Questão 15 - Letra A -------------")
#gauss_jacobi(matriz15a, b15a, x15a, e)
#print("\n ----------- Questão 15 - Letra B -------------")
#gauss_jacobi(matriz15b, b15b, x15b, e)
#print("\n ----------- Questão 15 - Letra C -------------")
#gauss_jacobi(matriz15c, b15c, x15c, e)
#print("\n ----------- Questão 15 - Letra D -------------")
#gauss_jacobi(matriz15d, b15d, x15d, e)
#print("\n ----------- Questão 16 - Letra A -------------")
#gauss_jacobi(matriz16a, b16a, x16a, e)
#print("\n ----------- Questão 16 - Letra B -------------")
#gauss_jacobi(matriz16b, b16b, x16b, e)
#print("\n ----------- Questão 16 - Letra C -------------")
#gauss_jacobi(matriz16c, b16c, x16c, e)
#print("\n ----------- Questão 17 -------------")
#gauss_jacobi(matriz17, b17, x17, e)
#print("\n ----------- Questão 18 -------------")
#gauss_jacobi(matriz18, b18, x18, e)
#print("\n ----------- Questão 19 -------------")
#gauss_jacobi(matriz19, b19, x19, e)
#print("\n --------- Exemplo de Aula ------------------")
#gauss_jacobi(matriz, b, x, e)
gauss_jacobi(matriz1, b1, x1, e)
#gauss_jacobi(matriz2, b2, x2, e)
#gauss_jacobi(matriz3, b3, x3, e)