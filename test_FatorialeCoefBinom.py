# Implementação das funções fatorial e coefBinomial com execussão de bateria de testes automatizados para avaliar a consistência das implementações 

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
        C = ("em um coeficiente binomial n > p e p é pythonum número natural, portanto não há coeficiente binomial para os valores informados")
    if n>p and p >= 0:
        C = fatorial(n)//(fatorial(p)*fatorial(n-p))
    return C

def test_fatorialNEG():
    assert fatorial(-3) == ("somente numeros naturais possuem fatorial")

def test_fatorial0 ():
    assert fatorial (0)==1

def test_fatorial1 ():
    assert fatorial (1)==1

def test_fatorial2 ():
    assert fatorial (2)==2

def test_fatorial3 ():
    assert fatorial (3)==6

def test_fatorial4 ():
    assert fatorial (4)==24

def test_fatorial5 ():
    assert fatorial (5)==120

def test_coefBinomial5e2 ():
    assert coefBinomial (5,2)==10
