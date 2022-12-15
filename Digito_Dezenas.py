# Script que recebe um número inteiro inserido pelo usuário e informa o dígito das dezenas

numInt = int(input("Insira um número inteiro:"))
restoCentena = numInt%100
numDezena = restoCentena//10
print ("O dígito das dezenas é",numDezena)
