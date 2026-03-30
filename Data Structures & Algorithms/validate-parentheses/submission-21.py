class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = { "(" : ")", "[" : "]", "{" : "}" }

        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif stack and char == brackets[stack[-1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0


        