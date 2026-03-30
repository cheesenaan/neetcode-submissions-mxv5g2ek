class Solution:
    # Time Complexity: O(rows * cols)
    #   - Each cell is visited once due to memoization.
    #   - DFS explores at most 4 directions per cell.
    #
    # Space Complexity: O(rows * cols)
    #   - dp dictionary stores results for each cell.
    #   - Recursion stack can go as deep as rows * cols in worst case.

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # Number of rows and columns in the matrix
        rows, cols = len(matrix), len(matrix[0])

        # Possible movement directions: down, up, right, left
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        # Stores the final longest increasing path found
        res = 0

        # Memoization: (r, c) -> longest increasing path starting at (r, c)
        dp = {}

        def dfs(r, c):
            # If already computed, return cached result
            if (r, c) in dp:
                return dp[(r, c)]

            # Minimum path length is 1 (the cell itself)
            ans = 1

            # Try all 4 possible directions
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check bounds and increasing condition
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]
                ):
                    # Take the maximum path length from valid neighbors
                    ans = max(ans, 1 + dfs(nr, nc))

            # Cache result for current cell
            dp[(r, c)] = ans
            return ans        

        # Start DFS from every cell in the matrix
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))

        return res
