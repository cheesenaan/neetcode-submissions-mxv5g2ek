class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid:
            return 

        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # bfs at the same time from all treasure chests
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == INF
                        and grid[nr][nc] not in [0,-1]
                    ):
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))

        return 
                            




        