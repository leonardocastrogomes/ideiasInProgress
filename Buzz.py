# Script que recebe um número inteiro inserido pelo usuário e imprime 'Buzz' caso o número seja múltiplo de 5 ou o próprio número caso contrário

numeroInt = int(input('ínsira um número inteiro:'))
div5 = numeroInt%5
if div5 ==0:
    print ('Buzz')
else:
    print (numeroInt)
