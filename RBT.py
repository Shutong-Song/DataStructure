class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = None
    
class RBT:
    def __init__(self, root):
        self.root = root
        
    def left_rotate(self, x):
        """
        left rotate x node
        time complexity O(1)
        """
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
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
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x
        

if __name__ == "__main__":
    n1 = Node(3)
    n2 = Node(13)
    n3 = Node(99)
    n4 = Node(21)
    n5 = Node(7)
    n1.left = n2
    n2.left = n3
    n2.right = n4
    n1.right = n5
    root = RBT(n1)
    root.right_rotate(n1)
    print(n1.parent.val)
