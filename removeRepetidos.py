# função que recebe uma lista e remove os elementos repetidos

def remove_repetidos (x):
    n = len (x)
    lista = []
    while n>0:
        if x[0] in lista:
           del x[0]
        else:
            lista.append (x[0])
            del x[0]
        n = n-1
    lista.sort()
    return  lista
