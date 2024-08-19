#Implementar um algoritmo que implemente o Insertion Sort modo
#easy depois modo divertido (lista encadeada)

# Testar com elementos já ordenados
#• Testar com elementos ordenados na ordem inversa
#• Testar com elementos duplicados
#• Testar com elementos aleatórios sem repetição

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def sorted_insert(head, node):
    if head is None or head.data >= node.data:
        node.next = head
        return node
    else:
        current = head
        while current.next is not None and current.next.data < node.data:
            current = current.next
        node.next = current.next
        current.next = node
    return head


def insertion_sort_linked_list(ll):
    sorted_list = None
    current = ll.head
    while current is not None:
        next_node = current.next
        sorted_list = sorted_insert(sorted_list, current)
        current = next_node
    ll.head = sorted_list