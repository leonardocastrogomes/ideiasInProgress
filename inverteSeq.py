def lista():
    x = 1
    lista = []
    while x != 0:
        x = int(input("Digite um número: "))
        if x>1:
            lista.append (x)
    return lista
    
def inverte(x):
    n = len(x)
    listainvertida = []
    while n > 0:
        listainvertida.append (x[-1])
        del x[-1]
        n = n-1
    return listainvertida

def main ():
    y = lista ()
    y =inverte (y)
    print ("")
    for n in y:
        print (n)

main()
