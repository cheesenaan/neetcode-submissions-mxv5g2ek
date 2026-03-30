class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        res = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r,c):
            count = 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (matrix[nr][nc]) > (matrix[r][c])
                ):
                    count = max(count, 1 + dfs(nr, nc))

            return count

        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r,c))

        return res
        