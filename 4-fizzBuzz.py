numeroInt = int(input('insira um número inteiro:'))
div3 = numeroInt%3
div5 = numeroInt%5
if div3 ==0 and div5 ==0:
    print('FizzBuzz')
else:
    print(numeroInt)
