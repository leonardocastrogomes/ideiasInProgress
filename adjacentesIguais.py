numeroIn = input ('digite um número inteiro: ')
quantDigitos = len (numeroIn)
numeroIn = int(numeroIn)
nInicial = numeroIn
digitoA = 0
restoEsq = 0
digitoB = 0
nAdj = 0

while quantDigitos != 0:
    digitoA = numeroIn % 10
    restoEsq = numeroIn // 10
    digitoB = restoEsq % 10
    if digitoA == digitoB:
        nAdj = nAdj + 1
    quantDigitos = quantDigitos - 1
    numeroIn = restoEsq

if nAdj == 0:
    print('O número',nInicial,'não possui números adjacentes iguais')
else:
    print('O número',nInicial,'possui',nAdj, 'par(es) de números adjacentes iguais.')
