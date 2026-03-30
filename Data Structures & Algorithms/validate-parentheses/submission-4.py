class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hp = { "(" : ")", "[" : "]", "{" : "}" }

        print(hp.keys())

        for char in s:
            # if open bracket push to stack
            if char in hp.keys():
                print("append")
                stack.append(char)
            else:
                print("else")
                # if closing bracket then check
                if stack and char == hp[stack[-1]]:
                    print("stack is ", stack)
                    print("char is ", char)
                    print("peek stack is ", stack[-1])
                    print("hp value of peek stack is ", hp[stack[-1]])
                    stack.pop()
                else:
                    return False

        return len(stack) == 0







