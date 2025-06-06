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
            aux = sum(matriz[i, j] * x[j] for j in range(n) if j != i)
            #if np.isinf(aux) or np.isnan(aux):
                #raise ValueError(f"Overflow ou NaN detectado na iteração {iteracoes}, linha {i}")
            novo_x = (1 / matriz[i, i]) * (b[i] - aux)
            #if np.isinf(novo_x) or np.isnan(novo_x):
                #raise ValueError(f"Solução inválida na iteração {iteracoes}, linha {i}")
            dis_absoluta.append(novo_x - x[i])
            temp.append(novo_x)

        dis_rel = max(abs(np.array(dis_absoluta))) / max(abs(np.array(temp)))
        x = np.array(temp)
        np.savetxt('vetorX.txt', x, fmt='%.6f')
        iteracoes += 1

    residuo(matriz, b, x)
    print(f"Número de iterações: {iteracoes}")
    #else:
        #print("Encerrando execução devido à falta de dominância diagonal.")


# Dados de entrada
matriz1 = mmread('bcsstk22.mtx')
if not isinstance(matriz1, np.ndarray):
    matriz1 = matriz1.toarray()
b1 = np.random.uniform(1, 50, 138)
np.savetxt('vetorB_22.txt',  b1, fmt='%.6f')
x1 = np.zeros_like(b1)

matriz2 = mmread('bcsstk23.mtx')
if not isinstance(matriz2, np.ndarray):
    matriz2 = matriz2.toarray()
b2 = np.random.uniform(1, 50, 3134)
np.savetxt('vetorB_23.txt', b2, fmt='%.6f')
x2 = np.zeros_like(b2)

matriz3 = mmread('bcsstk24.mtx')
if not isinstance(matriz3, np.ndarray):
    matriz3 = matriz3.toarray()
b3 = np.random.uniform(1, 50, 3562)
np.savetxt('vetorB_24.txt', b3, fmt='%.6f')
x3 = np.zeros_like(b3)

matriz = np.array([
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
], dtype=float)

b = np.array([7, -8, 6], dtype=float)
x = np.array([0.7, -1.6, 0.6], dtype=float)
e = 0.01

#gauss_jacobi(matriz, b, x, e)
#gauss_jacobi(matriz1, b1, x1, e)
#gauss_jacobi(matriz2, b2, x2, e)
gauss_jacobi(matriz3, b3, x3, e)