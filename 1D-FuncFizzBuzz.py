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
