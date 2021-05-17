class Node:
    def __init__(self, key):
        self.val = key
        self.prev = None
        self.nex = None
        
        
class HashTable:
    def __init__(self, capacity = 256):
        """
        specify the capacity of the hash table, default is 256
        the hash table is a list
        """
        self.capa = capacity
        self.table = [None]*self.capa
        
    def _hash_val(self, key):
        return hash(key)%self.capa
    
    def insert_val(self, key):
        """
        insert key to hash table, O(1) time complexity
        """
        val = self._hash_val(key)
        if not self.table[val]:
            self.table[val] = Node(key)
        else:
            new_node = Node(key)
            head = self.table[val]
            new_node.nex = head
            head.prev = new_node
            self.table[val] = new_node
            
    def delete_val(self, key):
        """
        delete key from hash table using search_val function
        if key not exists, raise error
        O(1) time complextiy
        """
        temp_node = self.search_val(key)
        val = self._hash_val(key)
        if not temp_node:
            raise KeyError(f"key:{key} not exists!")
        if temp_node.prev:
            temp_node.prev.nex = temp_node.nex
        if temp_node.nex:
            temp_node.nex.prev = temp_node.prev
        if (not temp_node.prev) and (not temp_node.nex):
            self.table[val] = None
            
    def search_val(self, key):
        """
        search the key, if exists, return the node(which is a doubly-linked node)
        if not exists, return None
        O(n) worst-case time complexity
        """
        val = self._hash_val(key)
        if not self.table[val]:
            return 
        head = self.table[val]
        dummy = head
        while dummy:
            if dummy.val == key:
                return dummy
                    
            
            
if __name__ == "__main__":
    ht = HashTable(256)
    ht.insert_val("James")
    ht.insert_val("Lily")
    ht.insert_val("Emma")
    ht.delete_val("Emma")
    ht.delete_val("Lily")
    ht.delete_val("James")
    