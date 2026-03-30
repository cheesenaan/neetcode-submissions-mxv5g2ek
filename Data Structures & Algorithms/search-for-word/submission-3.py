class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Get the number of rows and columns in the board
        row, col = len(board), len(board[0])

        def backtrack(r, c, i):
            """
            r, c = current cell position
            i = current index in the word we are trying to match
            """

            # Base Case:
            # If we've matched all characters in 'word', return True
            if i == len(word):
                return True

            # Boundary checks + character mismatch check:
            # If out of bounds OR current board cell is not the character we want
            if (
                r < 0 or c < 0 or 
                r >= row or c >= col or 
                board[r][c] != word[i]
            ):
                return False

            # Temporarily mark this cell as visited so we don’t reuse it
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all 4 possible directions (up, down, left, right)
            res = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )

            # Restore the cell for future paths (backtracking)
            board[r][c] = temp

            return res
        
        # Try starting the search from every cell in the grid
        for r in range(row):
            for c in range(col):
                # If any start point returns True, the word exists
                if backtrack(r, c, 0):
                    return True

        # If no path matched the entire word
        return False
