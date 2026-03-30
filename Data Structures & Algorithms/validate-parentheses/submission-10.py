class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        brackets = { "(" : ")", "[" : "]", "{" : "}" }

        # if opening brackets, push to stack
        # if closing bracket, check if closing bracket is value of key for last item in stack
        # check if stack is empty

        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            else:
                if stack and  bracket == brackets[stack[-1]]:
                        stack.pop()
                else:
                    return False

        return len(stack) == 0

