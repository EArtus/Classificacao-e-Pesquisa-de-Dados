class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def delete_node(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif(key > root.val):
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)
    return root

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def main():
    root = None
    while True:
        print("1. Inserir elemento")
        print("2. Deletar elemento")
        print("3. Buscar elemento")
        print("4. Exibir árvore em-ordem")
        print("5. Exibir árvore em pré-ordem")
        print("6. Exibir árvore em pós-ordem")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            key = int(input("Informe um valor a ser inserido: "))
            root = insert(root, key)
        elif opcao == '2':
            key = int(input("Informe o valor a ser deletado: "))
            root = delete_node(root, key)
        elif opcao == '3':
            key = int(input("Informe o valor a ser buscado: "))
            res = search(root, key)
            if res is None:
                print("Valor não encontrado.")
            else:
                print("Valor encontrado.")
        elif opcao == '4':
            print("Árvore em-ordem:", end=' ')
            inorder(root)
            print()
        elif opcao == '5':
            print("Árvore em pré-ordem:", end=' ')
            preorder(root)
            print()
        elif opcao == '6':
            print("Árvore em pós-ordem:", end=' ')
            postorder(root)
            print()
        elif opcao == '7':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
