import math

def pesquisa_por_salto(lista, elemento):
    n = len(lista)
    passo = int(math.sqrt(n))
    prev = 0

    while lista[min(passo, n) - 1] < elemento:
        prev = passo
        passo += int(math.sqrt(n))
        if prev >= n:
            return -1

    while lista[prev] < elemento:
        prev += 1
        if prev == min(passo, n):
            return -1

    if lista[prev] == elemento:
        return prev

    return -1

lista = [int(x) for x in input("Digite uma lista de números ordenados separados por espaço: ").split()]
elemento = int(input("Digite o número que deseja buscar: "))
indice = pesquisa_por_salto(lista, elemento)

if indice != -1:
    print(f"Elemento encontrado no índice: {indice}.")
else:
    print("Elemento não encontrado na lista.")
