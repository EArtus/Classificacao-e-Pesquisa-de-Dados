class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableWithLinkedLists:
    def __init__(self, size):
        self.size = size
        self.table = {i: None for i in range(size)}
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)
        
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = new_node
    
    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def __str__(self):
        result = {}
        for key, node in self.table.items():
            values = []
            current = node
            while current:
                values.append((current.key, current.value))
                current = current.next
            result[key] = values
        return str(result)



htable = HashTableWithLinkedLists(10)
htable.insert("name", "Alice")
htable.insert("age", 25)
print(htable.search("age"))  
print(htable)
