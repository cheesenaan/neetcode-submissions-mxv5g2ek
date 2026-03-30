class Solution:
    def isValid(self, s: str) -> bool:

        hp = {'{' : '}', '(' : ')', '[' : ']'}
        stack = []

        for char in s:
            if char in hp.keys():
                stack.append(char)
            elif stack and char == hp[stack[-1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0 

        