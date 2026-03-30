class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        self.res = 0

        def dfs(r, c):
            stack = []
            stack.append((r,c))
            self.res += 1
            while stack:
                r, c = stack.pop()
                grid[r][c] = '0'
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == '1'
                    ):
                        stack.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)

        return self.res


        

        