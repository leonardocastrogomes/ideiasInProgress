# App que recebe parâmetros da assinatura de autoria de um texto qualquer e 'n' textos inseridos
# pelo usuário e informa qual dos textos possui a maior probabilidade de ser um plágio.
# Implementa também a função calcula_assinatura (texto) que permitem o cálculo da assinatura de estilo em um texto
# e a função compara_assinatura (a,b) que recebe duas assinaturas e calcula o índice de semelhança entre os textos.
# Minha implementação para o exercício de conclusão do curso Introdução à Ciência da Computação com Python
# oferecido pelo IME/USP na plataforma Coursera.

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos. Primeira função a ser executada no programa.
    Uma variável deve armazenar
        '''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    ind0 = abs(as_a[0] - as_b[0])
    ind1 = abs(as_a[1] - as_b[1])
    ind2 = abs(as_a[2] - as_b[2])
    ind3 = abs(as_a[3] - as_b[3])
    ind4 = abs(as_a[4] - as_b[4])
    ind5 = abs(as_a[5] - as_b[5])
    indice = (ind0+ind1+ind2+ind3+ind4+ind5)/6
    return indice

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto. '''
    sentencas = separa_sentencas (texto)
    n_sentencas = len(sentencas)
    n_frases = 0
    listaPalavras = []
    palavras = []
    mediaCharXFrase = 0
    for n in sentencas:
        frases = separa_frases(n)
        n_frases += len(frases)
        for k in frases:
            listaPalavras += separa_palavras (k)
            palavras += k
            mediaCharXFrase += len (k)
    n_palavras = len(listaPalavras)
    caracteres = len(palavras)-(len(listaPalavras)-1)
    diferentes = n_palavras_diferentes (listaPalavras)
    unicas = n_palavras_unicas (listaPalavras)
    wal = caracteres / n_palavras
    ttr = diferentes / n_palavras
    hlr = unicas / n_palavras
    sal = ((len(palavras)+(n_frases - n_sentencas)) / n_sentencas)
    sac = n_frases / n_sentencas
    pal = mediaCharXFrase / n_frases
    assign = [wal, ttr, hlr, sal, sac, pal]
    return assign
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    contador = 0
    indice = 100
    for n in textos:
        contador += 1
        assign = calcula_assinatura (n)
        var = compara_assinatura (assign, ass_cp)
        if var < indice:
            indice = var
            resultado = contador
    return resultado


fb = le_assinatura ()
provas = le_textos ()
resultado = avalia_textos (provas, fb)
print("O autor do texto", resultado,"está infectado com COH-PIAH")
