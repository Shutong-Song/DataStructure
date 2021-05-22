class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        

class BST:
    def __init__(self, root):
        self.root = root
        
    def search_iter(self, key):
        """
        search a node by value
        """
        if not self.root:
            return
        dummy = self.root
        while dummy:
            if dummy.val == key:
                return dummy
            if dummy.val > key:
                dummy = dummy.left
            else:
                dummy = dummy.right
                
    def minimum_iter(self, node = None):
        """
        find the minimum node of a BST, return the node
        """
        if not node:
            node = self.root
        dummy = node
        if not dummy:
            return
        while dummy.left:
            dummy = dummy.left
        return dummy
    
    
    def maximum_iter(self, node = None):
        """
        find the maximum node and return it
        """
        if not node:
            node = self.root
        dummy = node
        if not dummy:
            return
        while dummy.right:
            dummy = dummy.right
        return dummy
    
    
    def successor(self, node):
        """
        The smallest value that larger than the input node
        return the node associated with that value
        """
        if node.right:
            return self.minimum_iter(node.right)
        node_y = node.parent
        while node_y and node == node_y.right:
            node = node_y
            node_y = node_y.parent
        return node_y
    
    def predecessor(self, node):
        """
        the largest value that smaller than the input node
        return the node associated with that value
        """
        if node.left:
            return self.maximum_iter(node.left)
        node_y = node.parent
        while node_y and node == node_y.left:
            node = node_y
            node_y = node_y.parent
        return node_y
    
    def insert_node(self, node):
        """
        insert a node to the proper leaf location
        """
        dummy = self.root
        node_p = None
        while dummy:
            node_p = dummy
            if node.val < dummy.val:
                dummy = dummy.left
            else:
                dummy = dummy.right
        node.parent = node_p
        if not node_p:
            self.root = node
        if node_p.val > node.val:
            node_p.left = node
        else:
            node_p.right = node
            
    def _transplant(self, node_u, node_v):
        """
        replace node_u with node_v at a BST
        """
        if not node_u.parent:
            self.root = node_v
        elif node_u.parent.left == node_u:
            node_u.parent.left = node_v
        else:
            node_u.parent.right = node_v
        if node_v:
            node_v.parent = node_u.parent
            
    def delete_node(self, node_z):
        """
        delete a node has a few situations:
        1. node_z has no left node
        2. node_z has no right node
        3. node_z has both left and right nodes
        """
        if not node_z.left: #node_z has no left node
            self._transplant(node_z, node_z.right)
        elif not node_z.right: # node_z has no right node
            self._transplant(node_z, node_z.left)
        else: # node_z has both left and right nodes
            node_y = self.minimum_iter(node_z.right)
            if node_y.parent != node_z:
                self._transplant(node_y, node_y.right)
                node_y.right = node_z.right
                node_y.right.parent = node_y
            self._transplant(node_z, node_y)
            node_y.left = node_z.left
            node_y.left.parent = node_y
                
        
        
        
    
    
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
    n12 = Node(14)
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
    bst = BST(n1)
    #key1 = 44 
    #find_node = bst.search_iter(key1)
    #print(find_node.val) if find_node else print("No such key!")
    #min_key = bst.minimum_iter()
    #print(min_key.val)
    #max_key = bst.maximum_iter()
    #print(max_key.val)
    #succ = bst.successor(n2)
    #print(succ.val) if succ else print("No successor")
    #prede = bst.predecessor(n11)
    #print(prede.val) if prede else print("No predecessor")
    #bst.insert_node(n12)
    bst.delete_node(n1)
    print(n3.parent.val)
    