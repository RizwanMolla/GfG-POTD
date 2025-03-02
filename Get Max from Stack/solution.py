class Solution:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []
        
    def push(self, x):
        self.main_stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        
    def pop(self):
        if self.main_stack:
            if self.main_stack[-1] == self.max_stack[-1]:
                self.max_stack.pop()
            self.main_stack.pop()
        
    def peek(self):
        return self.main_stack[-1] if self.main_stack else -1

    def getMax(self):
        return self.max_stack[-1] if self.max_stack else -1