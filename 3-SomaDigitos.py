numeroN = input('Digite um número inteiro:')
nAlg = len(numeroN)
numeroN = int(numeroN)
dígito = 0
restoEsq = 0
somaDigitos = 0

while nAlg > 0:
    digito = numeroN % 10
    restoEsq = numeroN // 10
    somaDigitos = somaDigitos + digito
    numeroN = restoEsq
    nAlg = nAlg - 1

print (somaDigitos)
