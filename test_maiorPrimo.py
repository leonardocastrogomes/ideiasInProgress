# Implementação das funções eh_Primo(n) e maiorPrimo(k) com bateria de testes automatizados para avaliar a consistência das funções

def eh_Primo(n):
    import math
    divisor = int(math.sqrt (n))
    if n<2:
        primo = False
    else:
        primo = True
    teste = 1
    while n>3 and divisor >= 2:
        teste= n%divisor
        divisor = divisor-1
        if teste == 0:
            primo = False

def maiorPrimo (k):
    if k < 2:
        RGmaiorPrimo = ("insira um número maior ou igual a 2")
    else:
        if k ==2:
            RGmaiorPrimo = 2
        if k==3:
            RGmaiorPrimo = 3
        if k>3:
            while eh_Primo(k) == False:
                RGmaiorPrimo = k-1
                k = k-1
    return RGmaiorPrimo

def maiorPrimoNeg ():
    assert maiorPrimo(-1)== ("ïnsira um número maior ou igual a 2")

def maiorPrimo0 ():
    assert maiorPrimo(0)== ('insira um número maior ou igual a 2')

def maiorPrimo1 ():
    assert maiorPrimo(1)== ('insira um número maior ou igual a 2')

def maiorPrimo2 ():
    assert maiorPrimo(2) == 2

def maiorPrimo3 ():
    assert maiorPrimo(3) == 3

def maiorPrimo4 ():
    assert maiorPrimo (4) == 3

def maiorPrimo5 ():
    assert maiorPrimo (5) == 5

def maiorPrimo6 ():
    assert maiorPrimo (6) == 5

def maiorPrimo7 ():
    assert maiorPrimo (7)== 7

def maiorPrimo8 ():
    assert maiorPrimo (8)== 7

def maiorPrimo9 ():
    assert maiorPrimo (9)== 7

def maiorPrimo10 ():
    assert maiorPrimo (10)== 7

def maiorPrimo11 ():
    assert maiorPrimo (11)== 11

def maiorPrimo12 ():
    assert maiorPrimo (12)== 11

def maiorPrimo13 ():
    assert maiorPrimo (13)== 13

def maiorPrimo14 ():
    assert maiorPrimo (14)== 13

def maiorPrimo15 ():
    assert maiorPrimo (15)== 13

def maiorPrimo16 ():
    assert maiorPrimo (16)== 13

def maiorPrimo17 ():
    assert maiorPrimo (17)== 17

def maiorPrimo18 ():
    assert maiorPrimo (18)== 17

def maiorPrimo19 ():
    assert maiorPrimo (19) == 19

def maiorPrimo20 ():
    assert maiorPrimo (20)== 19

def maiorPrimo21 ():
    assert maiorPrimo (21)== 19

def maiorPrimo22 ():
    assert maiorPrimo (22)== 19

def maiorPrimo23 ():
    assert maiorPrimo (23)== 23

def maiorPrimo24 ():
    assert maiorPrimo (24)== 23

def maiorPrimo25 ():
    assert maiorPrimo (25)== 23

def maiorPrimo26 ():
    assert maiorPrimo (26)== 23

def maiorPrimo27 ():
    assert maiorPrimo (27)== 23

def maiorPrimo28 ():
    assert maiorPrimo (28)== 23

def maiorPrimo29 ():
    assert maiorPrimo (29)== 29

def maiorPrimo30 ():
    assert maiorPrimo (30)== 29

def maiorPrimo100 ():
    assert maiorPrimo (100)== 97
