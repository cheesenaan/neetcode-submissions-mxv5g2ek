class Solution:
    def isValid(self, s: str) -> bool:

        # if opening bracket push to stack
        # else pop and check if current bracket is pop value
        # check if stack is empty or not

        from collections import deque
        stack = deque()
        brackets = { "(" : ")", "[" : "]", "{" : "}" }


        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif stack and brackets[stack[-1]] == bracket:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0



       
