class Solution:
    def isValid(self, s: str) -> bool:

        from collections import deque
        stack = deque() # garanteed O(1) time complexity compared to using lists (arrays)
        hp = { "(" : ")", "[" : "]", "{" : "}" }

        for char in s:
            # if open bracket push to stack
            if char in hp.keys():
                stack.append(char)
            else:
                # if closing bracket then check
                if stack and char == hp[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0









