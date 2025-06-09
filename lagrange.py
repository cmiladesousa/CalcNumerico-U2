import sympy as sp

def lagrange(x, vetorx, vetory):
    pn = 0
    for i in range(len(vetory)):
        lk = 1
        for j in range(len(vetorx)):
            if i != j:
                lk *= (x - vetorx[j])/(vetorx[i] - vetorx[j])
        pn += vetory[i] * lk
    return sp.simplify(pn)

# Entradas

# Visto em sala
vetorx = [-1, 0, 2]
vetory = [4, 1, -1]

# Questão 21
vetorx21 = [ 0.4, 0.6, 0.8]
vetory21 = [1.5735, 2.0333, 2.6965]
x21 = 0.75

# Questão 23
vetorx23 = [0, 6, 10]
vetory23 = [6.67, 17.33, 42.67]
x23 = 7
y23 = 10

# Questão 24
vetorx24 = [1990, 2000, 2010]
vetory24 = [335, 370, 388]
x24 = 2008
y24 = 350

# Questão 25

vetorx25 = [2008, 2011, 2014]
vetory25 = [323, 1430, 7310]
x25a = 2010
x25b = 2015
y25 = 5000

#Foi utilizado a biblioteca sympy para gerar o polinômio e calcular o valor de f(x) e x

print("\n Questão dada em aula")
x = sp.Symbol('x')
polinomio = lagrange(x, vetorx, vetory)
print("P(x) = ", polinomio)

print("P(1) = ", polinomio.subs(x, 1))

print("\n Questão 21")
x = sp.Symbol('x')
polinomio = lagrange(x, vetorx21, vetory21)
print("P(x) = ", polinomio)

print("P(0.75) = ", polinomio.subs(x, x21))

print("\n Questão 23")
x = sp.Symbol('x')
polinomio = lagrange(x, vetorx23, vetory23)
print("P(x) = ", polinomio)

print("P(7) = ", polinomio.subs(x, x23))

solucoes = sp.solve(polinomio - y23, x)
print("P(x) = 10: ", solucoes)

print("\n Questão 24")
x = sp.Symbol('x')
polinomio = lagrange(x, vetorx24, vetory24)
print("P(2008) = ", polinomio)

print("P(7) = ", polinomio.subs(x, x24))

solucoes = sp.solve(polinomio - y24, x)
print("P(x) = 350: ", solucoes)

print("\n Questão 25")
x = sp.Symbol('x')
polinomio = lagrange(x, vetorx25, vetory25)
print("P(x) = ", polinomio)

print("P(2010) = ", polinomio.subs(x, x25a))

print("P(2015) = ", polinomio.subs(x, x25b))

solucoes = sp.solve(polinomio - y25, x)

print("P(x) = 5000: ", solucoes)
