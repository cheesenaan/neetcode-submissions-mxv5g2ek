class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res = 0

        def dfs(r, c):
            stack = []
            stack.append((r,c))
            grid[r][c] = 0
            area = 1
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 0
                        stack.append((nr, nc))
                        area += 1
            return area

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            area = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 0
                        q.append((nr, nc))
                        area += 1

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))

        return res

