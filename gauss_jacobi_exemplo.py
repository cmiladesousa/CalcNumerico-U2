import numpy as np

# Dados de entrada
matriz = np.array([
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
], dtype=float)

b = np.array([7, -8, 6], dtype=float)
x = np.array([0.7, -1.6, 0.6], dtype=float)

# Parâmetros
e = 0.01
iteracoes = 0
isDominante = False
contador = 0

for i in range(len(matriz)):
    total_linha = 0
    total_coluna = 0
    for j in range(len(matriz)):
        if i != j:
            total_linha += matriz[i][j]
            total_coluna += matriz[j][i]
    if matriz[i][i] > total_linha or matriz[i][i] > total_coluna:
        contador += 1

if contador == len(matriz):
    isDominante = True
else:
    print("Não convergiu! A matriz não é diagonalmente dominante")

# Inicialização dos erros
dis_absoluta = [float('inf')]
dis_rel = float('inf')
residuo =[]

# Iteração
if isDominante:
    while (max(abs(np.array(dis_absoluta))) > e or dis_rel > e) and iteracoes < 500:
        temp = []
        dis_absoluta = []
        for i in range(len(matriz)):
            aux = 0
            for j in range(len(matriz)):
                if j != i:
                    aux += matriz[i][j] * x[j]
            novo_x = (1 / matriz[i][i]) * (b[i] - aux)
            dis_absoluta.append(novo_x - x[i])
            temp.append(novo_x)

        dis_rel = max(abs(np.array(dis_absoluta))) / max(abs(np.array(temp)))
        x = np.array(temp)
        iteracoes += 1

    # Resíduo
    for i in range(len(matriz)):
        soma_residuo = 0
        for j in range(len(matriz)):
            soma_residuo += matriz[i][j] * x[j]
        residuo.append(soma_residuo - b[i])

    print("\nResultado final dos valores de x:")
    print(x)
    residuo = [float(r) for r in residuo]

    print(max(residuo))
    print(f"Número de iterações: {iteracoes}")
else:
    print("Encerrando execução devido à falta de dominância diagonal.")