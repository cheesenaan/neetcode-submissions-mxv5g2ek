class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        stack = []

        def backtracking(opened, closed):

            if opened == closed == n:
                return ans.append(''.join(stack))

            if opened < n:
                stack.append('(')
                backtracking(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(')')
                backtracking(opened, closed + 1)
                stack.pop()

        backtracking(0 ,0 )
        return ans  



        