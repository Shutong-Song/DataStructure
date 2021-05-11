class Stack:
    def __init__(self):
        self.s = []
        self.sz = 0
        self.top_element = None
     
    # 1. stack operation: push, pop
    def push(self, element):
        self.s.append(element)
        self.sz += 1
        if self.sz != 0: 
            self.top_element = self.s[-1]
     
    def pop(self):
        if self.sz > 0: 
            self.s.pop()
            self.sz -= 1
            if self.sz > 0:
                self.top_element = self.s[-1]
            else:
                self.top_element = None
        else:
            print("stack underflow!")
            self.top_element = None
         
     
    # 2. stack element access: top(or peek)
    def top(self):
        return self.top_element
     
    # 3. stack other methods: empty, size
    def empty(self):
        if self.sz == 0:
            return True
        return False
     
    def size(self):
        return self.sz