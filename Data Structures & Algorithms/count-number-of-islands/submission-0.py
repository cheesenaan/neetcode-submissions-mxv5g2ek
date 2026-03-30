class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        res = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = r+dr, c+dc
                    if (
                        newR in range(rows)
                        and newC in range(cols)
                        and (newR,newC) not in visited
                        and grid[newR][newC] == '1'
                    ):
                        q.append((newR,newC))
                        visited.add((newR,newC))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    res += 1
        return res
                    




        