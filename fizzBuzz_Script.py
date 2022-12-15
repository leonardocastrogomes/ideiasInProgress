# Script que recebe um número inserido pelo usuário e imprime 'FizzBuzz' caso o número seja simultâneamente múltiplo de 3 e 5 
# ou o próprio número em caso contrário 

numeroInt = int(input('insira um número inteiro:'))
div3 = numeroInt%3
div5 = numeroInt%5
if div3 ==0 and div5 ==0:
    print('FizzBuzz')
else:
    print(numeroInt)
