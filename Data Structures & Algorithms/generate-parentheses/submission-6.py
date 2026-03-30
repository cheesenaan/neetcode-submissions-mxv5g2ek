class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        stack = []
        
        def backtrack(closed, opened):
            if closed == opened == n:
                return ans.append(''.join(stack))

            if opened < n:
                stack.append('(')
                backtrack(closed, opened + 1)
                stack.pop()

            if closed < opened:
                stack.append(')')
                backtrack(closed + 1, opened)
                stack.pop()

        backtrack(0 , 0)
        return ans

       