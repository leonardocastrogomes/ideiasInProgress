# função principal

def main():
    '''
    Inicializa o jogo NIM oferecendo ao usuário a possibilidade de escolher entre
    os modos Partida ou Campeonato
    '''
    #corpo da função main
    print ('Bem-vindo ao jogo do NIM! Escolha:')
    print ('')
    print ('1 - para jogar uma partida isolada')
    modo = int(input('2 - para jogar um campeonato')) 
    if modo == 1:
        print ('')
        print ('Voce escolheu uma partida!')
        partida()
    if modo == 2:
        print ('')
        print ('Voce escolheu um campeonato!')
        print ('')
        campeonato()
        
# Declaração das funções


def partida():
    '''
    Executada quando o usuário escolhe o modo Partida
    '''
    #corpo partida
    print ("")
    n = int(input("Quantas peças?"))
    while n<=0:
        print ("Insira um número natural para o jogo funcionar")
        print ("")
        n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    while m>n or m<=0:
        print ("O limite deve ser um número natural menor que a quantidade de peças")
        print ("")
        m = int(input("Limite de peças por jogada?"))
        
    if n%(m+1)==0:
        print ("")
        print ("Você começa!")
        print ("")
        retira = usuario_escolhe_jogada (n,m)
        fim_do_lance_usuario (retira)
        n = n-retira
        conta_pecas (n)
        print ("")
        vez = "comp"

    else:
        print ("")
        print ("Computador começa!")
        print ("")
        retira = computador_escolhe_jogada (n,m)
        fim_do_lance_computador (retira)
        n = n-retira
        conta_pecas (n)
        print ("")
        vez = "user"
        

    while n > m:
        if vez == "comp":
            retira = computador_escolhe_jogada (n,m)
            fim_do_lance_computador (retira)
            n = n-retira
            conta_pecas (n)
            print ("")
            vez = "user"
        else:
            retira = usuario_escolhe_jogada (n,m)
            fim_do_lance_usuario (retira)
            n = n-retira
            conta_pecas (n)
            print ("")
            vez = "comp"
    retira = computador_escolhe_jogada (n,m)
    fim_do_lance_computador (retira)
    resultado_partida ()
    print ("")

def campeonato():
    '''
    Executada quando o usuário escolhe o modo Campeonato
    '''
    #corpo campeonato
    print ("**** Rodada 1 ****")
    print ("")
    partida ()
    print ("**** Rodada 2 ****")
    print ("")
    partida()
    print ("**** Rodada 3 ****")
    print ("")
    partida()
    resultado_campeonato()
    



def computador_escolhe_jogada (n,m):
    '''
    Analisa os parâmetro n e m para definir quantas peças o computador deve retirar
    e garantir que restará sempre uma quantidade m+1 de peças no tabuleiro no
    ultimo lance do usuário antes do fim da partida. Retorna um inteiro  
    '''
    #corpo computador_escolhe_jogada
    if 0<n<m:
        retira = n
        return retira
    else:
        multiplo = n//(m+1)
        retira = n-(multiplo*(m+1))
        if retira !=0:
            return retira
        else:
            return m


                
def usuario_escolhe_jogada (n,m):
    '''
    Solicita que o usuário escolha uma jogada válida.
    '''
    if m>n or n==m or n<=0 or m<=0:
        return
        print ("Oops! Jogada invalida!Tente denovo")
        print ("")

    else:
        retira = int(input('Quantas peças você vai tirar?'))
        while retira > m or retira <= 0:
            print ("Oops! Jogada invalida!Tente denovo")
            print ("")
            retira = int(input('Quantas peças você vai tirar?'))
        return retira


def resultado_partida():
    '''
    Utilizada para imprimir o resultado da partida e encerrar o jogo
    '''
    #corpo resultado_partida
    print ('Fim do jogo! O computador ganhou!')



def resultado_campeonato():
    '''
    Utilizada para imprimir o resultado do campeonato e encerrar o jogo
    '''
    #corpo resultado_campeonato
    print ('**** Final do campeonato! ****')
    print ('')
    print ('Placar: Você 0x3 Computador')



def fim_do_lance_computador(k):
    testa = k
    if testa>1:
        diz = print ("O computador tirou", testa, "peças")
        return diz
    if testa==1:
        diz = print ("O computador tirou uma peça")
        return diz

def fim_do_lance_usuario(x):
    if x>1:
        diz = print ("Você tirou", x, "peças")
        return diz
    if x==1:
        diz = print ("Você tirou uma peça")
        return diz

def conta_pecas(x):
    if x==1:
        print("Agora resta apenas uma peça.")
    else:
        print("Agora restam apenas", x,"peças.")

main()
