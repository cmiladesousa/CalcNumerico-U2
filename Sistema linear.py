def determinante(matriz):
    """Calcula o determinante de uma matriz quadrada usando expansão de Laplace (recursivo)."""
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
    """Cria a matriz aumentada [A | b]"""
    return [linha + [b[i]] for i, linha in enumerate(A)]

def rank(matriz):
    """Calcula o posto (rank) de uma matriz usando eliminação de Gauss."""
    if not matriz or not matriz[0]:
        return 0

    # Cópia da matriz para não alterar a original
    temp = [linha[:] for linha in matriz]
    linhas = len(temp)
    colunas = len(temp[0])
    rank = 0

    for i in range(colunas):
        # Procurar linha com valor diferente de zero
        for j in range(rank, linhas):
            if temp[j][i] != 0:
                temp[rank], temp[j] = temp[j], temp[rank]
                break
        else:
            continue  # Nenhuma linha útil nesta coluna

        for j in range(rank + 1, linhas):
            if temp[j][i] != 0:
                fator = temp[j][i] / temp[rank][i]
                for k in range(i, colunas):
                    temp[j][k] -= fator * temp[rank][k]

        rank += 1

    return rank

def gauss_eliminacao(A, b):
    n = len(b)
    if len(A) != n:
        print("❌ Erro: número de equações (linhas de A) diferente do número de termos independentes (b).")
        return None
    # Criação da matriz aumentada
    Ab = [A[i][:] + [b[i]] for i in range(n)]

    # Calcular posto (rank)
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

    # Eliminação de Gauss com pivotamento parcial
    for i in range(n):
        # Procurar linha com maior valor na coluna i
        max_linha = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_linha][i]):
                max_linha = k

        if A[max_linha][i] == 0:
            print("❌ Pivô zero encontrado. Sistema sem solução única.")
            return None

        A[i], A[max_linha] = A[max_linha], A[i]
        b[i], b[max_linha] = b[max_linha], b[i]

        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]
            b[j] -= fator * b[i]

    # Substituição regressiva
    x = [0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - soma) / A[i][i]

    return x

# EXEMPLO DE USO

# Teste com solução única:
#A = [ [2, 1, -1], [-3, -1, 2], [-2, 1, 2] ]
#b = [8, -11, -3]

# # Teste com infinitas soluções:
#A = [ [1, -2, 1], [2, -4, 2], [3, -6, 3] ]
#b = [0, 0, 0]

# # Teste sem solução:
#A = [ [3, 3, 3],  [2, 2, 2],  [4, 4, 4] ]
#b = [6, 12, 19]

solucao = gauss_eliminacao([linha[:] for linha in A], b[:])  # cópia para evitar alterar A e b

if solucao:
    print("\n✅ Solução encontrada:")
    for i, valor in enumerate(solucao):
        print(f"x{i+1} = {valor:.2f}")