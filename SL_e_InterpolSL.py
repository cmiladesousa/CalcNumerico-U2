def determinante(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    if n == 2:
        return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]

    det = 0
    for c in range(n):
        submatriz = [linha[:c] + linha[c+1:] for linha in matriz[1:]]
        det += ((-1)**c) * matriz[0][c] * determinante(submatriz)
    return det

def matriz_aumentada(A, b):
    return [linha + [b[i]] for i, linha in enumerate(A)]

def rank(matriz):
    if not matriz or not matriz[0]:
        return 0

    temp = [linha[:] for linha in matriz]
    linhas = len(temp)
    colunas = len(temp[0])
    rank = 0

    for i in range(colunas):
        for j in range(rank, linhas):
            if temp[j][i] != 0:
                temp[rank], temp[j] = temp[j], temp[rank]
                break
        else:
            continue

        for j in range(rank + 1, linhas):
            if temp[j][i] != 0:
                fator = temp[j][i] / temp[rank][i]
                for k in range(i, colunas):
                    temp[j][k] -= fator * temp[rank][k]

        rank += 1

    return rank

def eliminacao_gauss_com_pivotamento(A, b):
    n = len(b)
    A = [linha[:] for linha in A]  # cópia para não alterar original
    b = b[:]
    
    for i in range(n):
        max_linha = max(range(i, n), key=lambda k: abs(A[k][i]))
        if A[max_linha][i] == 0:
            raise ValueError("❌ Pivô zero encontrado. Sistema sem solução única.")
        A[i], A[max_linha] = A[max_linha], A[i]
        b[i], b[max_linha] = b[max_linha], b[i]

        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]
            b[j] -= fator * b[i]

    x = [0] * n
    for i in reversed(range(n)):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - soma) / A[i][i]

    return x

def gauss_eliminacao(A, b):
    n = len(b)
    if len(A) != n:
        print("❌ Erro: número de equações (linhas de A) diferente do número de termos independentes (b).")
        return None

    Ab = [A[i][:] + [b[i]] for i in range(n)]

    rank_A = rank([linha[:] for linha in A])
    rank_Ab = rank([linha[:] for linha in Ab])

    print(f"Posto(A) = {rank_A}, Posto([A|b]) = {rank_Ab}")

    if rank_A < rank_Ab:
        print("❌ Sistema sem solução. Encerrando o programa.")
        return None
    elif rank_A == rank_Ab and rank_A < n:
        print("⚠️ Sistema com infinitas soluções. Encerrando o programa.")
        return None
    else:
        print("✅ Sistema pode ter solução única. Continuando...")

    return eliminacao_gauss_com_pivotamento(A, b)

def construir_matriz_vandermonde(x):
    n = len(x)
    return [[xi ** i for i in range(n)] for xi in x]

def interpolacao_sistema_linear(x, y):
    if len(x) != len(y):
        raise ValueError("x e y devem possuir o mesmo tamanho")
    if len(set(x)) != len(x):
        raise ValueError("x deve conter somente valores distintos")

    A = construir_matriz_vandermonde(x)
    coeficientes = eliminacao_gauss_com_pivotamento(A, y)
    return coeficientes

def avaliar_polinomio(coef, x):
    return sum(c * (x ** i) for i, c in enumerate(coef))

# ========== EXEMPLOS DE USO ==========

# Escolha qual bloco você quer ativar para testar:

### 1. Teste de sistema linear:
#A = [[−9, 5, 6], [2, 3, 1], [−1, 1, −3]]  
#b = [11, 4, −2]
#A = [[2, −1, 1], [3, 3, 9], [3, 3, 5]]
#b = [-1, 0, 4]
#A = [[0.252 0.36 0.12], [0.112 0.16 0.24], [0.147 0.21 0.25]]
#b = [7, 8, 9]
#A = [[3, −2, 5, 1], [−6, 4, −8, 1], [9, −6, 19, 1], [6, −4, −6, 15]]
#b = [7, −9, 23, 11]
#A = [[1, 1, −1, 2, −1], [2, 0, 0, 0, 0], [0, 2, 0, 0, 0], [4, 0, 0, 16, 0], [0, 0, 4, 0, 0]]
#b = [2, 2, 2, 20, 4]
#A = [[1, 2, 1], [2, −1, 2], [3, 1, 3]]  
#b = [1, 2, 4]
#A = [[0, 15, 1, 3], [15, 2, 2, 3], [0, 4, 15, 1], [1, 2, 2, 15]]
#b = [-3, 4, 7, 5]

solucao = gauss_eliminacao([linha[:] for linha in A], b[:])
if solucao:
    print("\n✅ Solução encontrada:")
    for i, valor in enumerate(solucao):
        print(f"x{i+1} = {valor:.4f}")

### 2. Interpolação
x_pontos = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
y_pontos = [1.0, 1.2408, 1.5735, 2.0333, 2.6965, 3.7183]

coef = interpolacao_sistema_linear(x_pontos, y_pontos)
print("\nCoeficientes do polinômio interpolador:", coef)

x_test = 0.75
print(f"Valor do polinômio em x = {x_test}:", avaliar_polinomio(coef, x_test))
