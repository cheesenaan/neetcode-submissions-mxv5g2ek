class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(matrix), len(matrix[0])
        
        def dfs(r, c):
            ans = 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and matrix[nr][nc] > matrix[r][c]
                ):
                    ans = max(ans, 1 + dfs(nr, nc))

            return ans

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r,c))

        return res
        