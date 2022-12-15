# Script que recebe os parâmetros de uma função de segundo grau e calcula as raizes da equação

import math
a = int(input("Qual é o valor de A na equação de segundo grau?:"))
b = int(input("Qual é o valor de B na equação de segundo grau?:"))
c = int(input("Qual é o valor de C na equação de segundo grau?:"))
delta = (b**2)-(4*a*c)
if delta <0:
    print ("esta equação não possui raízes reais")
if delta == 0:
    raizX = (-b)/(2*a)
    print ("a raiz desta equação é",raizX)
if delta > 0:
    raizX = ((-b) + (math.sqrt((b**2)-(4*a*c))))/(2*a)
    raizX1 = ((-b) - (math.sqrt((b**2)-(4*a*c))))/(2*a)
    maior = raizX < raizX1
    if maior == True:
        print ("as raízes da equação são", raizX, "e", raizX1)
    else:
        print ("as raízes da equação são", raizX1, "e", raizX)
