from typing import List
from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {"+", "-", "*", "/"}
        stack = deque()

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if stack:
                    b = stack.pop() 
                    a = stack.pop() if stack else 0

                    if token == '+':
                        stack.append(int(a) + int(b))
                    elif token == '-':
                        stack.append(int(a) - int(b))
                    elif token == '*':
                        stack.append(int(a) * int(b))
                    elif token == '/':
                        stack.append(int(a) / int(b))

        return int(stack[0])