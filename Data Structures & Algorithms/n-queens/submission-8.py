class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.' for i in range(n)] for _ in range(n) ]
        cols, posD, negD = set(), set(), set()
        res = []

        def dfs(r):
            if r == n:
                return res.append([''.join(row) for row in board])

            for c in range(n):
                if c in cols or (r+c) in posD or (r-c) in negD:
                    continue 

                cols.add(c)
                posD.add((r+c))
                negD.add((r-c))
                board[r][c] = 'Q'
                dfs(r+1)
                cols.remove(c)
                posD.remove((r+c))
                negD.remove((r-c))
                board[r][c] = '.'

        dfs(0)
        return res
                 

        