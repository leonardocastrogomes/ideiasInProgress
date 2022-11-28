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
    i = k
    teste = eh_Primo(i)
    if teste == True:
        return i
    else:
        while teste == False:
                i = i-1
                teste = eh_Primo (i)
        return i
