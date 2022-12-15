# Script que recebe um número inserido pelo usuário e imprime 'Fizz' para múltiplos de 3 ou o próprio número em caso contrário

numeroInt = int(input('ínsira um número inteiro:'))
div3 = numeroInt%3
if div3 == 0:  
        print('Fizz')
else:
        print (numeroInt)        
