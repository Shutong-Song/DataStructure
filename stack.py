class Stack:
    def __init__(self):
        self.s = []
        self.sz = 0
     
    # 1. stack operation: push, pop
    def push(self, element):
        self.s.append(element)
        self.sz += 1
     
    def pop(self):
        if self.sz > 0: 
            self.s.pop()
            self.sz -= 1
        else:
            print("stack underflow!")
         
     
    # 2. stack element access: top(or peek)
    def top(self):
        return self.s[-1] if len(self.s) else None
     
    # 3. stack other methods: empty, size
    def empty(self):
        return True if self.sz == 0 else False
     
    def size(self):
        return self.sz