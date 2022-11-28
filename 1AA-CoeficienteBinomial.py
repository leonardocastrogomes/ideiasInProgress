
def fatorial(x):
    fatorialX = 1
    if x < 0:
        fatorialX = ("somente numeros naturais possuem fatorial")
    if x ==0 or x ==1:
        fatorialX = 1
    else:
        while x >= 2:
            fatorialX = (fatorialX)*(x)
            x = x - 1
    return fatorialX

def coefBinomial (n,p):
    C = 1
    if n<p or p<0:
        C = ("em um coeficiente binomial n > p e p é um número natural, portanto não há coeficiente binomial para os valores informados")
    if n>p and p >= 0:
        C = fatorial(n)//(fatorial(p)*fatorial(n-p))
    return C
