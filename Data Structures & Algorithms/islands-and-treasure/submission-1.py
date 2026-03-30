class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        INF = 2147483647

        q = deque()
        # bfs on every treasure chest
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        # run bfs each at the same time

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                newR = r + dr
                newC = c + dc
                if newR in range(rows) and newC in range(cols) and grid[newR][newC] == INF:
                    grid[newR][newC] = grid[r][c] + 1
                    q.append((newR, newC))

        return 






        