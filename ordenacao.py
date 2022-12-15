# Script que recebe três números inteiros inseridos pelo usuário e imprime 'crescente' se os números
# estão em uma sequencia crescente ou 'não crescente' caso contrário.

num1 = int(input('ínsira um número inteiro:'))
num2 = int(input('insira o segundo número inteiro:'))
num3 = int(input('insira mais um número inteiro:'))

if num1 < num2 and num2 < num3:
    print ('crescente')
else:
    print ('não está em ordem crescente')
