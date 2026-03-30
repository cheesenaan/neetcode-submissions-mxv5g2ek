class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid:
            return

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        INF = 2147483647
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == INF
                    ):
                        q.append((nr, nc))
                        grid[nr][nc] = grid[r][c] + 1

        return 


        
        