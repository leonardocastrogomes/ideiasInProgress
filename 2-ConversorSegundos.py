qtdSegundos = int(input("Por favor, entre a quantidade de segundos que deseja converter:"))
dias = qtdSegundos // (60*60*24)
horas = (qtdSegundos // (60*60))-(dias*24)
minutos = (qtdSegundos // 60)-((horas*60)+(dias*24*60))
segundos = qtdSegundos % 60
print (dias, "dias,",horas,"horas,", minutos, "minutos e", segundos, "segundos.")
