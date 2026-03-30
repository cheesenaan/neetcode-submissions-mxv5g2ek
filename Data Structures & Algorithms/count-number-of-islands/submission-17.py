class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0

        def dfs(r, c):
            q = deque()
            q.append((r,c))
            grid[r][c] = '#'

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == '1'
                    ):
                        q.append((nr ,nc))
                        grid[nr][nc] = '#'

             

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r,c)

        return res
                        