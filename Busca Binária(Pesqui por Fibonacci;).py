def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def pesquisa_fibonacci(lista, elemento):
    n = len(lista)
    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m1 + fib_m2

    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m1 + fib_m2

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)

        if lista[i] < elemento:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif lista[i] > elemento:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i

    if fib_m1 and offset + 1 < n and lista[offset + 1] == elemento:
        return offset + 1

    return -1

lista = [int(x) for x in input("Digite uma lista de números ordenados separados por espaço: ").split()]
elemento = int(input("Digite o número que deseja buscar: "))
indice = pesquisa_fibonacci(lista, elemento)

if indice != -1:
    print(f"Elemento encontrado no índice: {indice}.")
else:
    print("Elemento não encontrado na lista.")
