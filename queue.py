### queue implementation using python list

class Queue:
    def __init__(self, capacity):
        if int(capacity) <= 0:
            raise ValueError("capacity cannot less than 1")
        self.capacity = int(capacity)
        self.q = [None]*self.capacity
        self.head = -1
        self.tail = -1
        self.sz = 0
    
    # insert element into the tail of the queue
    def enqueue(self, element):
        if self.sz == self.capacity:
            print("Queue overflow!")
            return
        if self.tail == self.capacity - 1 and self.head != 0:
            self.tail = 0 
        else:
            if self.sz == 0:
                self.head += 1
            self.tail += 1
        self.q[self.tail] = element
        self.sz += 1
    
    # pop element from queue from the head
    def dequeue(self):
        if self.sz == 0:
            print("Queue underflow!")
            return
        if self.head == self.capacity - 1 and self.tail != 0:
            self.head = -1
        elif self.sz == 1:
            self.head = -1
            self.tail = -1
        else:
            self.head += 1
        self.sz -= 1
    
    # head element of the queue
    def front(self):
        if self.sz == 0:
            return
        return self.q[self.head]
    
    # tail element of the queue
    def back(self):
        if self.sz == 0:
            return
        return self.q[self.tail]
    
    # size of current queue
    def size(self):
        return self.sz
    
    # empty check
    def empty(self):
        return self.sz == 0
        
        
        
if __name__ == "__main__":
    q = Queue(3)
    q.dequeue()
    q.enqueue(2)
    q.enqueue(12)
    q.enqueue(32)
    q.enqueue(11)
    q.dequeue()
    q.dequeue()
    print(q.front())
    print(q.back())
    print(q.empty())
    