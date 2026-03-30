class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.' for i in range(n)] for _ in range(n)]
        cols, posDiag, negDiag = set(), set(), set()
        res = []

        def dfs(r):
            if r == n:
                return res.append([''.join(row) for row in board])

            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue 

                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'
                dfs(r+1)
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        dfs(0)
        return res
