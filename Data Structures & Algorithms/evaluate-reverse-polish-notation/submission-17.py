from typing import List
from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        

        for token in tokens:
            if token not in ['+', '-', '/', '*']:
                stack.append(token)
            else:
                a, b = stack.pop(), stack.pop()

                if token == '+':
                    stack.append(int(a) + int(b))
                elif token == '-':
                    stack.append(int(b) - int(a))
                elif token == '*':
                    stack.append(int(a) * int(b))
                elif token == '/':
                    stack.append(int(b) / int(a))

        
        print(stack)
        return int(stack[0])





        