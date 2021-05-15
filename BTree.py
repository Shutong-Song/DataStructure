class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BTree:
    def __init__(self, root):
        self.root = root 
        
    def inorder_iter(self, res):
        """
        inorder tree traversal using stack
        store traversal elements in "res"
        """
        if self.root:
            stack = []
            while True:
                while self.root:
                    stack.append(self.root)
                    self.root = self.root.left
                if not stack:
                    break
                node = stack.pop()
                print(node.val)
                res.append(node.val)
                self.root = node.right
    
    def preorder_iter(self, res):
        if self.root:
            stack = [self.root]
            while stack:
                node = stack.pop()
                res.append(node.val)
                print(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                
    
    def postorder_iter(self, res):
        if self.root:
            stack = [self.root]
            while stack:
                node = stack.pop()
                res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res = res[::-1]
            print(res)
    
    def inorder_recur(self, root, res):
        if root:
            self.inorder_recur(root.left, res)
            print(root.val)
            res.append(root.val)
            self.inorder_recur(root.right, res)
    
    def preorder_recur(self, root, res):
        if root:
            print(root.val)
            res.append(root.val)
            self.preorder_recur(root.left, res)
            self.preorder_recur(root.right, res)
    
    def postorder_recur(self, root, res):
        if root:
            self.postorder_recur(root.left, res)
            self.postorder_recur(root.right, res)
            print(root.val)
            res.append(root.val)


if __name__ == "__main__":
    root = Node(7)
    n1 = Node(12)
    n2 = Node(9)
    n3 = Node(33)
    n4 = Node(91)
    n5 = Node(7)
    n6 = Node(5)
    root.left = n1
    root.right = n2
    n1.left = n3
    n3.right = n6
    n2.left = n4
    n2.right = n5
    bt = BTree(root)
    res = []
    # inorder iterative
    # bt.inorder_iter(res)
    
    # preorder iterative
    # bt.preorder_iter(res)
    
    # postorder iterative
    # bt.postorder_iter(res) 
    
    # inorder recursive
    # bt.inorder_recur(root, res) 
    
    # preorder recursive
    # bt.preorder_recur(root, res) 
    
    # postorder recursive
    bt.postorder_recur(root, res)