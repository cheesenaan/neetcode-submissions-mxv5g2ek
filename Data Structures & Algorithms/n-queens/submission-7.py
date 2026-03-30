class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # ------------------------------------------------------------
        # Time Complexity:
        #   O(n!) 
        #   - We try to place one queen per row.
        #   - For each row, we try up to n columns.
        #   - Many branches are pruned early due to column/diagonal conflicts,
        #     but in the worst case the complexity is factorial.
        #
        # Space Complexity:
        #   O(n^2)
        #   - Board uses O(n^2) space.
        #   - Column set + diagonal sets use O(n).
        #   - Recursion depth is O(n).
        # ------------------------------------------------------------

        # Tracks which columns already have queens
        col = set()

        # Tracks positive diagonals (r + c)
        posD = set()

        # Tracks negative diagonals (r - c)
        negD = set()

        # Initialize empty chess board
        board = [['.' for j in range(n)] for _ in range(n)]

        # Stores all valid board configurations
        res = []

        def backtrack(r):
            # If we've placed queens in all rows, we found a valid solution
            if r == n:
                # Convert board rows to strings and store the solution
                res.append([''.join(row) for row in board])
                return

            # Try placing a queen in every column of the current row
            for c in range(n):

                # If column or diagonals are already occupied, skip
                if c in col or (r + c) in posD or (r - c) in negD:
                    continue

                # Place queen: mark column and diagonals as occupied
                col.add(c)
                posD.add(r + c)
                negD.add(r - c)
                board[r][c] = 'Q'

                # Move to the next row
                backtrack(r + 1)

                # Backtrack: remove queen and free the column/diagonals
                col.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
                board[r][c] = '.'

        # Start backtracking from the first row
        backtrack(0)

        return res
