def busca_binaria_iterativa(lista, elemento):
    inicio, fim = 0, len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

lista = [int(x) for x in input("Digite uma lista de números ordenados separados por espaço: ").split()]
elemento = int(input("Digite o número que deseja buscar: "))
indice = busca_binaria_iterativa(lista, elemento)

if indice != -1:
    print(f"Elemento encontrado no índice {indice}.")
else:
    print("Elemento não encontrado na lista.")
