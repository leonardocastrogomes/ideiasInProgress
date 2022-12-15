# script que recebe um número inteiro inserido pelo usuário e informa se este número é primo ou não primo

import math

numeroN = int(input('Digite um número inteiro:'))
divisor = int(math.sqrt (numeroN))
primo = True
teste = 1

if numeroN <= 1:
    primo = False

while numeroN>3 and divisor >= 2:
    teste= numeroN%divisor
    divisor = divisor-1
    if teste == 0:
        primo = False

if primo == False:
    print ('não primo')
else:
    print ('primo')
