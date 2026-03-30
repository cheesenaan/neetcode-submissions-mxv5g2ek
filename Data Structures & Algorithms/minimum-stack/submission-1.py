
class MinStack:
    from collections import deque

    def __init__(self):
        self.stack = deque()
        
    # garanteed O(1) time
    def push(self, val: int) -> None:
        self.stack.append(int(val))
        
    # garanteed O(1) time
    def pop(self) -> None:
        self.stack.pop()
        
    # garanteed O(1) time
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        m = self.stack[0]
        for s in self.stack:
            if s < m:
                m = s

        return m



        
