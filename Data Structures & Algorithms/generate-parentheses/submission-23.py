class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res, cur = [], []

        def backtracking(closed, opened, n):
            if closed == opened == n:
                res.append(''.join(cur))

            if opened < n:
                cur.append('(')
                backtracking(closed, opened+1, n)
                cur.pop()

            if closed < opened:
                cur.append(')')
                backtracking(closed+1, opened, n)
                cur.pop()

        backtracking(0,0,n)
        return res
        