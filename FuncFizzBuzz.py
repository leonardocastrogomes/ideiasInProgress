# Função que recebe um número inteiro e imprime 'Fizz' para números múltiplos de 3, 
# 'Buzz' para múltiplos de 5, 'FizzBuzz' para múltiplos de 3 e 5 ou o número inteiro
# caso não seja múltiplo nem de 3 e nem de 5.

def fizzbuzz (k):
    numeroInt = k
    div3 = numeroInt%3
    div5 = numeroInt%5
    if div3 == 0 and div5 ==0:
        result= "FizzBuzz"
    if div3 == 0 and div5 !=0:
        result= "Fizz"
    if div3 != 0 and div5 ==0:
        result= "Buzz"
    if div3 !=0 and div5 !=0:
        result= numeroInt

    return result
