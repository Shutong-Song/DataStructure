class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.nex = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.sz = 0

    def insert_node(self, anode):
        """
        insert a node to the head of the list, O(1) time complexity
        """
        if self.head:
            anode.nex = self.head
            self.head.prev = anode
        self.head = anode
        self.sz += 1

    def delete_node(self, anode):
        """
        delete a node at any place if exists in the list
        """
        if anode.prev:
            anode.prev.nex = anode.nex
            self.sz -= 1
        if self.head == anode:
            self.head = self.head.nex
            self.sz -= 1
        if anode.nex:
            anode.nex.prev = anode.prev

    def traversal(self):
        dummy = self.head
        while dummy:
            print(dummy.val)
            dummy = dummy.nex

    def size(self):
        return self.sz

    def top(self):
        if self.head:
            return self.head.val

    def search(self, key):
        dummy = self.head
        while dummy:
            if dummy.val == key:
                return True
        return False



if __name__ == "__main__":
    node1 = Node(3)
    node2 = Node(12)
    node3 = Node(99)
    dlist = DoublyLinkedList()
    dlist.delete_node(node3)
    dlist.insert_node(node1)
    dlist.insert_node(node2)
    dlist.insert_node(node3)
    dlist.delete_node(node1)
    dlist.traversal()
    print(dlist.top())

        