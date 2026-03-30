class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        #2:51

        current = []
        ans = []

        def backtrack(closed, opened):
            if closed == opened == n:
                ans.append(''.join(current))
                return

            if opened < n:
                current.append('(')
                backtrack(closed, opened + 1)
                current.pop()

            if closed < opened:
                current.append(')')
                backtrack(closed + 1, opened)
                current.pop()

            
        backtrack(0 , 0)
        return ans
