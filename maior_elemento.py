def maior_elemento (x):
    maior = x[0]
    for n in x:
        if n > maior:
            maior = n
    return maior
