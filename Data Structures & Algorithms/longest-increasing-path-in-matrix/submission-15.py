class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ans = 0
        def dfs(r, c):
            res = 1            
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and matrix[r][c] < matrix[nr][nc]
                ):
                    res = max(res, 1 + dfs(nr, nc))
            return res

        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))

        return ans




            
        