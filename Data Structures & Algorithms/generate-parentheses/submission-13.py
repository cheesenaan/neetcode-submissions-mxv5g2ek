class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        stack = []

        def backtrack(opened, closed):
            if opened == closed == n:
                return ans.append(''.join(stack))

            if opened < n :
                stack.append('(')
                backtrack(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(')')
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0,0)
        return ans


        