class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res, cur = [], []

        def dfs(opened, closed, n):
            if opened == closed == n:
                return res.append(''.join(cur[:]))

            if opened < n:
                cur.append('(')
                dfs(opened+1, closed, n)
                cur.pop()

            if closed < opened:
                cur.append(')')
                dfs(opened, closed+1, n)
                cur.pop()

        dfs(0,0,n)
        return res        