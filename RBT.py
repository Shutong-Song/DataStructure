class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = None
    
class RBT:
    def __init__(self, root, nil):
        self.root = root
        self.nil = nil
        
    def left_rotate(self, x):
        """
        left rotate x node
        time complexity O(1)
        """
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        
    def right_rotate(self, y):
        """
        right rotate y
        time complexity O(1)
        """
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x
        
    def insert_node(self, z):
        """
        insert a node to the Red-black tree
        time complexity O(lg(n)) where n is the number of nodes
        """
        node_p = self.nil
        dummy = self.root
        while dummy != self.nil:
            node_p = dummy
            if dummy.val > z.val:
                dummy = dummy.left
            else:
                dummy = dummy.right
                
        z.parent = node_p
        if node_p == self.nil:
            self.root = z.parent
        elif node_p.val > z.val:
            node_p.left = z
        else:
            node_p.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = "red"
        self.insert_fixup(z)
    
    def insert_fixup(self, z):
        """
        fix up the violation of RBT properties
        """
        while z.parent.color == "red": # if z.parent.color = "black" all property hold, function do nothing
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "red": #if z's uncle is red, and z.parent is red, j
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black"
        
                    
                    
            
        
        
        
if __name__ == "__main__":
    n1 = Node(23)
    n2 = Node(13)
    n3 = Node(9)
    n4 = Node(15)
    n5 = Node(27)
    nil = Node(float("inf"))
    nil.color = "black"
    n1.parent = nil 
    n1.color = "black"
    n1.left = n2
    n2.left = n3
    n2.right = n4
    n2.parent = n1
    n2.color = "black"
    n1.right = n5
    n5.parent = n1
    n3.left = nil
    n3.right = nil
    n3.parent = n2
    n3.color = "red"
    n4.left = nil
    n4.right = nil
    n4.parent = n2
    n4.color = "red"
    n5.left = nil
    n5.right = nil
    n5.color = "black"
    root = RBT(n1, nil)
    
    #insert node
    n6 = Node(14)
    root.insert_node(n6)
    print(n4.left.val)
    