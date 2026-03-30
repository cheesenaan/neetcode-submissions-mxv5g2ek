class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # find all groups of O's touching border and convert to T

        def dfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                r,c = q.popleft()
                board[r][c] = 'T'
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and board[nr][nc] == 'O'
                    ):
                        q.append((nr, nc))
                        board[r][c] = 'T'

        # convert all O -> T
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or r == rows-1 or c == 0 or c == cols-1):
                    dfs(r,c)

        # convert all O -> X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'


        # convert all T -> O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        return 