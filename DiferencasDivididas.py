import time

def tabelamento (grau, F):
    """
    Esta função faz a leitura dos pontos x e y e monta uma tabela com eles.

    :param grau: grau do polinômio
    :type grau: int
    :param F: Lista de listas das diferenças divididas
    :type F: list
    """
    # Inicializando o tabelamento:
    tabelax = []
    tabelay = []

    # Leitura dos pontos x e y (quantidade de pontos = n+1):
    for i in range(grau+1):
        x = float(input(f"Digite x{i}: "))
        y = float(input(f"Digite y{i}: "))
        tabelax.append(x)
        tabelay.append(y)
    F.append(tabelay.copy()) #primeira coluna com os valores de y

    #Exibição do tabelamento:
    print("\nTabela (x, y):")
    for xi, yi in zip(tabelax, tabelay):
        print(f"x = {xi:.6f}, y = {yi:.6f}")

    return tabelax, tabelay

def exibicao_coeficientes(coeficientes):
    """
    Esta função exibe os valores dos coeficientes calculados do polinômio desejado.

    :param coeficientes: lista dos coeficientes
    :type coeficientes: list
    """
    contador = 0
    for valor in coeficientes:
        print(f"d{contador} = {valor:.6f}")
        contador +=1
################################################## INÍCIO ALGORITMO #########################################################        
inicio = time.time()
# Leitura do grau do polinômio:
n = int(input("\nDigite o grau do polinômio: "))

F = [] #tabela das diferenças divididas
x, y = tabelamento(n, F)
  
#Tabela triangular das diferenças divididas:
for i in range (1, n+1):
    ordem = []
    for j in range(n+1-i):
        diferencas = (F[i-1][j+1] - F[i-1][j]) / (x[j+i] - x[j])
        ordem.append(diferencas)
    F.append(ordem)

coeficientes = [] #lista de coeficientes do polinômio de grau n
for i in range(n+1):
    coeficientes.append(F[i][0])

print("\nLista de coeficientes é:")
exibicao_coeficientes(coeficientes)

#Exibição do polinômio na forma expandida
print("\nPolinômio de Newton na forma expandida é:")
print("P(x) = ", end="")
for i in range(len(coeficientes)):
    coef = coeficientes[i]
    if i == 0:
        termo = f"{coef:.6f}"  # primeiro termo
    else:
        sinal = "+" if coef >= 0 else "-"  
        termo = f" {sinal} {abs(coef):.6f}"  #Próximos termos
    for j in range(i):
        if x[j] >= 0:
            termo += f"*(x - {x[j]:.6f})"
        else:
            termo += f"*(x + {abs(x[j]):.6f})"
    print(termo, end="")
print()

#Calculo de P(x):
ponto = float(input("\nDigite o ponto x que quer avaliar:"))
resultado = 0
for i in range(len(coeficientes)):
    termo = coeficientes[i]
    for j in range(i):
        termo = termo*(ponto - x[j]) #produtório
    resultado = resultado + termo #somatório
print(f"\nResultado de P({ponto:.6f}) = {resultado:.6f}") #P(ponto)
fim = time.time()
print(f"\nTempo de execução: {fim - inicio:.6f} segundos")