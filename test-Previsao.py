# Script que recebe respostas do usuário a um quiz e imprime resultados possíveis

ehFeriado = input ("É feriado? (y/n):")
fazSol = input ("Faz Sol? (y/n):")
if ehFeriado == 'y' and fazSol == 'y':
    print ("Ok, vamos à praia")
if ehFeriado == "n" and fazSol == 'y':
    print ("Maldito capitalismo que nos obriga a trabalhar")
if ehFeriado== "y" and fazSol == 'n':
    print("Xii, sujou, deixemos a praia pra outro dia")
if ehFeriado == "n" and fazSol == 'n':
    print("Ok, só nos resta trabalhar")
    
