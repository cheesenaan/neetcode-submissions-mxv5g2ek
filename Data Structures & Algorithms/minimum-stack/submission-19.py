
class MinStack:
    from collections import deque

    def __init__(self):
        self.stack = [] #O(1) time and space
        self.minStack = [] #O(1) time and space
        
    def push(self, val: int) -> None: #O(1) time and space
        self.stack.append(val) 
        self.minStack.append(min(self.minStack[-1] , val ) if self.minStack else val)
        
    def pop(self) -> None: #O(1) time and space
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int: #O(1) time and space
        return self.stack[-1]
        
    def getMin(self) -> int: #O(n) time and space
        return self.minStack[-1]



        
