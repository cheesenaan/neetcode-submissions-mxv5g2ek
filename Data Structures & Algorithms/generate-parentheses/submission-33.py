class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res, cur = [], []
        
        def backtrack(opened, closed, n):
            if opened == closed == n:
                return res.append(''.join(cur[:]))

            if opened < n:
                cur.append('(')
                backtrack(opened+1, closed, n)
                cur.pop()

            if closed < opened:
                cur.append(')')
                backtrack(opened, closed+1, n)
                cur.pop()

        backtrack(0,0,n)
        return res


        