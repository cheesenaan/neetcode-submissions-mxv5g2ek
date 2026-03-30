class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # bfs from all 0 at same time
        
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()
        visit = set()
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        level = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == INF
                    ):
                        q.append((nr, nc))
                        grid[nr][nc] = level
            level += 1
        
        return 



        

        