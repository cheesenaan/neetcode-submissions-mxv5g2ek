
class MinStack:
    from collections import deque

    def __init__(self):
        self.stack = deque()
        self.minStack =  deque()
        
    # garanteed O(1) time
    def push(self, val: int) -> None:
        self.stack.append(int(val))
        self.minStack.append(min(self.minStack[-1] if self.minStack else val, int(val)))
        
    # garanteed O(1) time
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    # garanteed O(1) time
    def top(self) -> int:
        return self.stack[-1]
        
    # O(n) time
    def getMin(self) -> int:
        return self.minStack[-1]



        
