
class Node:
    def __init__(self, val):
        self.val = val
        self.nex = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.sz = 0

    def insert(self, anode):
        """
        insert a node into the head of list, O(1) time complexity
        """
        anode.nex = self.head
        self.head = anode
        self.sz += 1

    def insert_val(self, data):
        """
        insert a node based on value into the head of list, O(1) time complexity
        """
        anode = Node(data)
        anode.nex = self.head
        self.head = anode
        self.sz += 1

    def delete(self, anode):
        """
        delete a node from any place of the list, time complexity O(n) where n is the size of the linked list
        """
        if not self.head:
            return
        dummy = Node(0)
        dummy.nex = self.head
        final_node = dummy
        while dummy.nex:
            if dummy.nex == anode:
                dummy.nex = dummy.nex.nex
                self.sz -= 1
                break
            dummy = dummy.nex 
        self.head = final_node.nex

    def delete_val(self, data):
        """
        delete a node based on its value from the list, 
        if the data is not in the list, do nothing, otherwise delete the node
        """
        if not self.head:
            return 
        dummy = Node(0)
        dummy.nex = self.head
        final_node = dummy
        while dummy.nex:
            if dummy.nex.val == data:
                dummy.nex = dummy.nex.nex
                self.sz -= 1
                break
            dummy = dummy.nex
        self.head = final_node.nex
        
    def traversal(self):
        dummy = self.head
        while dummy:
            print(dummy.val)
            dummy = dummy.nex

    def top(self):
        """
        return the value of the head node if exists
        """
        if self.head:
            return self.head.val


    def size(self):
        return self.sz
    
    
if __name__ == "__main__":
    node1 = Node(3)
    node2 = Node(7)
    node3 = Node(13)
    s1 = SinglyLinkedList()
    s1.delete(node2)
    s1.insert(node1)
    s1.insert(node2)
    s1.insert(node3)
    s1.traversal()
    s1.delete(node1)
    s1.delete(node2)
    s1.delete(node3)
    print(s1.top())
    print(s1.size())

