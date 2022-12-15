# Função que calcula o fatorial de um número inteiro inserido pelo usuário

numeroN = int(input('Digite o valor de n:'))
fatorialN = numeroN

if numeroN ==0:
    fatorialN = 1
else:
    while numeroN >= 2:
        fatorialN = (fatorialN)*(numeroN-1)
        numeroN = numeroN - 1

print (fatorialN)
