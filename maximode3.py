# Função que recebe três parâmetros e retorna o maior deles

def maximo (a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    if c>a and c>b:
        return c
    if a==b and a==c:
        return a
