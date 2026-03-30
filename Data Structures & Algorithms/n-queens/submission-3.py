class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.' for i in range(n)] for _ in range(n)]
        cols, pD, nD = set(), set(), set()
        res = []

        def dfs(r):
            if r == n:
                return res.append([''.join(row) for row in board])

            for c in range(n):
                if c in cols or (r+c) in pD or (r-c) in nD:
                    continue 

                cols.add(c)
                pD.add((r+c))
                nD.add((r-c))
                board[r][c] = 'Q'
                dfs(r+1)
                cols.remove(c)
                pD.remove((r+c))
                nD.remove((r-c))
                board[r][c] = '.'

        
        dfs(0)
        return res

        
        