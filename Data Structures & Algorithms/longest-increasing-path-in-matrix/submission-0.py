class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0

        def dfs(r, c):
            ans = 1
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
            ):
                return
            
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]
                ):
                    ans = max(ans, 1 + dfs(nr, nc))

            return ans        


        for r in range(rows):
            for c in range(cols):
                ans = 0
                res = max(res, dfs(r,c))
        
        return res