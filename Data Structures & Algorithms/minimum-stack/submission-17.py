
class MinStack:
    from collections import deque

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(int(val))
        self.minStack.append(min(self.minStack[-1], int(val)) if self.minStack else int(val))

        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]



        
