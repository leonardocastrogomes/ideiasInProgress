# Função que um número inteiro inserido pelo usuário e devolve o maior número primo anterior caso o número informado não seja primo


def eh_Primo(n):
    import math
    if n>0:
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
    return primo

def maior_primo (k):
    teste = eh_Primo(k)
    if teste == True:
        return k
    else:
        while teste == False:
                k -= 1
                teste = eh_Primo (k)
        return k
