# Função que recebe uma lista de elementos e retorna a soma dos elementos

def soma_elementos (x):
    soma = 0
    for n in x:
        soma = soma + int(n)
    return soma
