class HashTableWithVectors:
    def __init__(self, size):
        self.size = size
        self.table = {i: [] for i in range(size)}
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))
    
    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
    
    def __str__(self):
        return str(self.table)



htable = HashTableWithVectors(10)
htable.insert("name", "Alice")
htable.insert("age", 25)
print(htable.search("name"))  
print(htable)
