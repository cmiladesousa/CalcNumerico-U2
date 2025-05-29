import numpy as np
from scipy.io import mmread
import random

#------------------------------------------- AUXILIARES --------------------------------------------
#Exibição de um vetor qualquer (6 casas decimais):
def exibir_vetor(vetor, nome):
    print("\nO vetor", nome, "é:")
    for valor in vetor:
        if abs(valor) < 1e-10:
            valor = 0.0
        print("[ {:.6f} ]".format(valor))

#--------------------------------------------- MATRIZ A --------------------------------------------
#Leitura da matriz A através dos arquivos do Matrix Market - considerar A como esparsa
A = np.array(mmread('bcsstk22.mtx').todense())
#A = np.array(mmread('bcsstk23.mtx').todense())
#A = np.array(mmread('bcsstk24.mtx').todense())
print("\nMatriz A lida.")

#--------------------------------------------- VETOR B ---------------------------------------------

#Criação do vetor B com valores aleatórios de 1 a 50:
B = np.random.randint(1, 51, size=A.shape[0])
print("\nVetor B criado.")

#Salvando o vetor B num txt:
#Caso arquivo bcsstk22.mtx usado:
np.savetxt('vetorB_22.txt', B, fmt='%.6f')

#Caso arquivo bcsstk23.mtx usado:
#np.savetxt('vetorB_23.txt', B, fmt='%.6f')

#Caso arquivo bcsstk24.mtx usado:
#np.savetxt('vetorB_24.txt', B, fmt='%.6f')
print("\nArquivo txt com valores do vetor B foi criado.")

#-------------------------------------- FATORAÇÃO DA MATRIZ A --------------------------------------

print("\n----------------------- MONTANDO A MATRIZ A FATORADA ---------------------------")

#Ordem da matriz A:
n = A.shape[0]

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

#Cálculo por etapas:
for k in range(etapas):
    contador = k+1

    #Definição do pivô:
    pivo = A[k][k]

    for i in range (n):
        if (i > k):
            #Definição do multiplicador de cada linha abaixo do pivô:
            multiplicador = A[i][k] / pivo #DÚVIDA: se o pivô for zero?

            #Armazenando os multiplicadores na matriz L:
            L[i][k] = multiplicador

            #Atualização da linha i:
            for count in range (n):
                A[i][count] = A[i][count] - multiplicador * A[k][count]
           

print("\nMatriz A foi fatorada em", contador, "etapas.")
print("\nMatrizes L e U criadas.")

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

#Exibição do vetor X calculado:
exibir_vetor(X,"X")