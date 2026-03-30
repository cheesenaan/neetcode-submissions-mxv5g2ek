class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.' for j in range(n)] for _ in range(n)]

        cols = set()
        postD = set()
        negD = set()
        res = []

        def backtrack(r):
            if r == n:
                return res.append([''.join(row) for row in board])

            for c in range(n):
                if c in cols or (r+c) in postD or (r-c) in negD:
                    continue 

                cols.add(c)
                postD.add((r+c))
                negD.add((r-c))
                board[r][c] = 'Q'
                backtrack(r+1)
                cols.remove(c)
                postD.remove((r+c))
                negD.remove((r-c))
                board[r][c] = '.'


        backtrack(0)
        return res

                