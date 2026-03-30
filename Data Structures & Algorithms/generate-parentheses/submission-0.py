class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        #2:51

        current = []
        ans = []

        def backtrack(opened, closed):
            if opened == closed == n:
                ans.append(''.join(current))
                return

            if opened < n:
                current.append("(")
                backtrack(opened + 1, closed)
                current.pop()

            if closed < opened:
                current.append(")")
                backtrack(opened , closed + 1)
                current.pop()

        backtrack(0 ,0 )
        return ans
