#------------------------------------ AUXILIARES ------------------------------------
#Exibição de matriz qualquer (6 casas decimais):
def exibir_matriz(matriz, nome):
    print("\nA Matriz", nome, "é:")
    for linha in matriz:
        print("[", end=" ")
        for valor in linha:
            if abs(valor) < 1e-10:
                valor = 0.0
            print("{:.6f}".format(valor), end=" ")
        print("]")

#Exibição de um vetor qualquer (6 casas decimais):
def exibir_vetor(vetor, nome):
    print("\nO vetor", nome, "é:")
    for valor in vetor:
        if abs(valor) < 1e-10:
            valor = 0.0
        print("[ {:.6f} ]".format(valor))


#-------------------------------------- MATRIZ A --------------------------------------

print("\n------------------------------ ENTRADA DE DADOS ----------------------------------")
#"n" é o inteiro que representa a ordem da matriz A
n = int (input("\nDigite a ordem da matriz A: "))
#Matriz A iniciada como vazia
A = []

#Leitura da matriz A
print("\nDigite os valores da matriz A, um por um: ")
for i in range(n):
    linha = []
    for j in range(n):
        valorA = float(input("Elemento [{}][{}]: ".format(i, j)))
        linha.append(valorA)
    A.append(linha)

# Exibição da matriz A
exibir_matriz(A, "A")

#-------------------------------------- VETOR B --------------------------------------
#Inicialização do Vetor B:
B = []

#Leitura do vetor B:
print("\nDigite os valores do vetor B, um por um: ")
for i in range(n):
    valorB = float(input("Elemento [{}]: ".format(i)))
    B.append(valorB)
    
# Exibição do vetor B:
exibir_vetor(B, "B")


#--------------------------- MONTANDO A MATRIZ A FATORADA ----------------------------

print("\n----------------------- MONTANDO A MATRIZ A FATORADA ---------------------------")

L = []
for i in range(n):
    linha = []
    for j in range(n):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    L.append(linha)

#A quantidade de etapas da fatoração será n-1:
etapas = n - 1
if(etapas > 1):
    print("\nTeremos", etapas, "etapas.")
else:
    print("\nTeremos", etapas, "etapa.")

#Cálculo por etapas:
for k in range(etapas):
    print("\nEtapa:", k+1)

    #Definição do pivô:
    pivo = A[k][k]

    for i in range (n):
        if (i > k):
            #Definição do multiplicador de cada linha abaixo do pivô:
            multiplicador = A[i][k] / pivo

            #Armazenando os multiplicadores na matriz L:
            L[i][k] = multiplicador
            #Atualização da linha i:
            for count in range (n):
                A[i][count] = A[i][count] - multiplicador * A[k][count]
            #Desmarcar as duas linhas abaixo para teste:
            #print("\nA matriz A com linha", i+1, "atualizada será:")
            #exibir_matriz(A, "A")


    #Exibição da Matriz A fatorada na etapa k:
    print("\nA matriz A fatorada na etapa", k+1, "será:")
    exibir_matriz(A, "A")

print("\n---------------------- ENCONTRANDO AS MATRIZES 'U' E 'L' --------------------------")

#Exibir L e U:
exibir_matriz(L,"L")
exibir_matriz(A, "U")

#------------------------------
# Matriz U: A matriz U será igual à matriz A atualizada. 
# Para evitar aumentar a complexidade espacial do algoritmo, resolvemos reutilizar a 
# matriz A atualizada no lugar de criar a matriz U e fazer a cópia dos valores de A para U.
#-------------------------------

#-------------------------------- CÁLCULO DE Y, A PARTIR DE L*Y = B -----------------------------

print ("\n-------------------------------- CALCULANDO Y ------------------------------------")
#Inicialização do Vetor Y:
Y = []

#Atribuição prévia dos n valores do vetor Y com "None": 
for i in range(n):
    valorY = None
    Y.append(valorY)

#Valor de Y[0] = B[0]:
Y[0] = B[0]
contador = 1
for i in range (1, n):
    Y[i] = B[i]
    for j in range (contador):
        Y[i] = Y[i] - L[i][j]*Y[j]
  
    contador = contador + 1

#Exibição do vetor Y calculado:
exibir_vetor(Y,"Y")

#------------------------------- CÁLCULO DE X, A PARTIR DE U*X = Y -----------------------------

print("\n-------------------------------- CALCULANDO X ------------------------------------")

#Inicialização do Vetor X:
X = []

#Atribuição prévia dos n valores do vetor X com "None": 
for i in range(n):
    valorX = None
    X.append(valorX)

#O valor de X[n-1] = Y[n-1]:
X[n-1] = Y[n-1] / A[n-1][n-1]

#Lembrando que a matriz U é igual à matriz A atualizada!

for i in range(n-2, -1, -1): 
    soma = 0
    for j in range(i+1, n):
        soma += A[i][j] * X[j]  
    X[i] = (Y[i] - soma) / A[i][i]
   
    if abs(X[i]) < 1e-30:
        X[i] = 0.0

#Exibição do vetor X calculado:
exibir_vetor(X,"X")