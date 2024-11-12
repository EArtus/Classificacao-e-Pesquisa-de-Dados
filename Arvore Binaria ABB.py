class ProductNode:
    def __init__(self, product_id, name, description, price):
        self.left = None
        self.right = None
        self.product_id = product_id
        self.name = name 
        self.description = description
        self.price = price 

def insert(root, product_id, name, description, price):
    if root is None:
        return ProductNode(product_id, name, description, price)
    else:
        if root.product_id < product_id:
            root.right = insert(root.right, product_id, name, dscription, price)
        else:
            root.left = insert(root.right, product_id, name, dscription, price)
    return root

def search(product_id, root):
    if root is none or product_id == product_id:
        return root 
    if root.product_id < product_id:
        return search(root.right, product_id)

def delete(root, product_id):
    if root is None:
        return root
    if product_id < root.product_id:
        root.left = delete(root.left, product_id)
    elif product_id > root.product_id:
        root.right = delete(root.right, product_id)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp 
        elif root.right is None: 
            temp = root.left 
            root = None 
            return temp 
        temp = minValude(root.right)
        root.product_id = temp.product_id
        root.name = temp.name 
        root.description = temp.description
        root.price = temp.price 
        root.right = delete(root.right, temp.product_id)
    return root
    
        
def minValude(node):
    current = node 
    while cuurent.left is not None:
        current = current.left
    return current


def inorder(root): 
    if root:
        inorder(root.left)
        print(root)
        inorder(root.right)


