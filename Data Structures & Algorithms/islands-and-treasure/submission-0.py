class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]


        def bfs(r, c):
            visited = set()
            q = deque()
            q.append((r,c,0))
            visited.add((r,c))

            while q:
                r, c, d = q.popleft()
                if grid[r][c] not in [0,-1]:
                    grid[r][c] = min(grid[r][c], d)

                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc
                    if newR in range(rows) and newC in range(cols) and (newR, newC) not in visited and grid[newR][newC] not in [0,-1]:
                        q.append((newR, newC, d+1))
                        visited.add((newR, newC))


        # bfs on every treasure chest
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r,c)

        return 






        