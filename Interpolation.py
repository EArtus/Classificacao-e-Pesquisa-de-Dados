def pesqBin(lista,chave):
    esq = 0
    dir = len(lista) - 1

    while esq <= dir:
        meio = (dir + esq) // 2

        if lista[meio] == chave: 
            return meio 

        elif lista[meio] > chave: 
            dir = meio - 1

        elif lista[meio] < chave:
            esq = meio + 1

    return -1

lista = [1, 10 , 11, 14, 16, 20] 
chave = 20
ind = pesqBin(lista, chave)
print(ind)