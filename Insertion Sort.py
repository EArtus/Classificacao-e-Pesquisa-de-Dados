#Implementar um algoritmo que implemente o Insertion Sort modo
#easy depois modo divertido (lista encadeada)

# Testar com elementos já ordenados
#• Testar com elementos ordenados na ordem inversa
#• Testar com elementos duplicados
#• Testar com elementos aleatórios sem repetição

def insertion_sort(data):
    n = len(data)
    for j in range(1, n):
        tmp = data[j]
        i = j - 1
        while i >= 0 and data[i] > tmp:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = tmp


data = [1, 2, 3, 4, 5]
insertion_sort(data)
print(data)

data = [5, 4, 3, 2, 1]
insertion_sort(data)
print(data)

data = [5, 3, 2, 4, 1]
insertion_sort(data)
print(data)

data = [5, 3, 2, 5, 4, 1]
insertion_sort(data)
print(data)