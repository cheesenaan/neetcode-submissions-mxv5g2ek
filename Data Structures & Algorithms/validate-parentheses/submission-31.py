class Solution:
    def isValid(self, s: str) -> bool:

        brackets = { '(' : ')', '{' : '}', '[' : ']' }
        stack = []

        # of opening bracket, push to stack
        # if closed bracket, pop and comapre latest element in stack

        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif stack and brackets[stack[-1]] == bracket:
                stack.pop()
            else:
                return False

        return len(stack) == 0

        