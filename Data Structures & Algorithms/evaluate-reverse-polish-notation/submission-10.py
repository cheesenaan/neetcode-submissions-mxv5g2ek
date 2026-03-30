from typing import List
from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {"+", "-", "*", "/"}
        stack = deque()

        # if not operator, push to stack
        # else pop last two, compute and push result

        for token in tokens:
            print("stack is", stack)
            if token not in operators:
                stack.append(token)
            elif stack:
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

        