def busca_binaria_recursiva(lista, elemento, inicio, fim):
    if inicio > fim:
        return []
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == elemento:
        indices = [meio]
        i = meio - 1
        while i >= inicio and lista[i] == elemento:
            indices.append(i)
            i -= 1
        i = meio + 1
        while i <= fim and lista[i] == elemento:
            indices.append(i)
            i += 1
        return sorted(indices)
    
    elif lista[meio] < elemento:
        return busca_binaria_recursiva(lista, elemento, meio + 1, fim)
    
    else:
        return busca_binaria_recursiva(lista, elemento, inicio, meio - 1)

lista = [int(x) for x in input("Digite uma lista de números ordenados separados por espaço: ").split()]
elemento = int(input("Digite o número que deseja buscar: "))
indices = busca_binaria_recursiva(lista, elemento, 0, len(lista) - 1)

if indices:
    print(f"Elemento encontrado nos índices: {indices}.")
else:
    print("Elemento não encontrado na lista.")
