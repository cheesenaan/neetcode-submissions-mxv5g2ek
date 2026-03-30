class Solution:
    def isValid(self, s: str) -> bool:

        brackets = { "(" : ")", "[" : "]", "{" : "}" }

        from collections import deque
        stack = deque()

        # if open bracket, push to stack
        # else push and compare current to last item in stack. return false is not same
        # return boolean if size of stack is zero

        for bracket in s:  #O(n)
            if bracket in brackets.keys():
                stack.append(bracket) #O(1)
            else:
                if stack and bracket == brackets[stack[-1]]:
                    stack.pop()  #O(1)
                else:
                    return False

        return len(stack) == 0



        