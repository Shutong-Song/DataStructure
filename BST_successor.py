class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        

class BST:
    def search_iter(self, root, key):
        if not root:
            return
        dummy = root
        while dummy:
            if dummy.val == key:
                return dummy
            if dummy.val > key:
                dummy = dummy.left
            else:
                dummy = dummy.right
                
    def minimum_iter(self, root):
        if not root:
            return
        dummy = root
        while dummy.left:
            dummy = dummy.left
        return dummy
    
    def maximum_iter(self, root):
        if not root:
            return
        dummy = root
        while dummy.right:
            dummy = dummy.right
        return dummy
    
    def successor(self, node):
        if node.right:
            return self.minimum_iter(node.right)
        node_y = node.parent
        while node_y and node == node_y.right:
            node = node_y
            node_y = node_y.parent
        return node_y
    
    def predecessor(self, node):
        if node.left:
            return self.maximum_iter(node.left)
        node_y = node.parent
        while node_y and node == node_y.left:
            node = node_y
            node_y = node_y.parent
        return node_y
    
    
    
if __name__ == "__main__":
    n1 = Node(15)
    n2 = Node(6)
    n3 = Node(18)
    n4 = Node(3)
    n5 = Node(7)
    n6 = Node(17)
    n7 = Node(20)
    n8 = Node(2)
    n9 = Node(4)
    n10 = Node(13)
    n11 = Node(9)
    n1.left = n2
    n1.right = n3
    n2.parent = n1
    n3.parent = n1
    n2.left = n4
    n2.right = n5
    n4.parent = n2
    n5.parent = n2
    n4.left = n8
    n4.right = n9
    n8.parent = n4
    n9.parent = n4
    n5.right = n10
    n10.parent = n5
    n10.left = n11
    n11.parent = n10
    n3.left = n6
    n3.right = n7
    n6.parent = n3
    n7.parent = n3
    
    #search a key 13
    bst = BST()
    key1 = 44 
    find_node = bst.search_iter(n1, key1)
    print(find_node.val) if find_node else print("No such key!")
    min_key = bst.minimum_iter(n1)
    print(min_key.val)
    max_key = bst.maximum_iter(n1)
    print(max_key.val)
    succ = bst.successor(n5)
    print(succ.val) if succ else print("No successor")
    prede = bst.predecessor(n11)
    print(prede.val) if prede else print("No predecessor")
    