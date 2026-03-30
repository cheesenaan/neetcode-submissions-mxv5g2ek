class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]


        # convert O in not surrounded area to T
        # dfs resursive
        def capture1(r, c):
            if (
                r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O'
            ):
                return
            board[r][c] = 'T'
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        # dfs iterative
        def capture2(r, c):
            stack = []
            stack.append((r,c))

            while stack:
                r, c = stack.pop()

                if (r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O'):
                    continue 

                board[r][c] = 'T'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    stack.append((nr, nc))

         # dfs iterative
        
        def capture(r, c):
            q = deque()
            q.append((r,c))

            while q:
                r, c = q.pop()

                if (r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O'):
                    continue 

                board[r][c] = 'T'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    q.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols-1:
                    capture(r,c)

        # convert all O to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # convert T to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        