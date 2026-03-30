class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 

        
        rows, cols = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        # find not surrounded area and convert O->T
        def dfs(r,c):
            if (
                not (0 <= r < rows)
                or not (0 <= c < cols)
                or board[r][c] != 'O'
            ):
                return
            board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r,c+1)
            dfs(r, c-1)


        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1):
                    dfs(r,c)
        
        # convert all O -> X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # convert T->O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'