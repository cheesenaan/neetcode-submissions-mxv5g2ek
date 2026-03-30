class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        visited = []
        res = {} # (r,c) : area of island

        def bfs(r,c,i):
            q = deque()
            q.append((r,c))
            visited.append((r,c))
            res[i] = 1

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    newR = r+dr
                    newC = c+dc

                    if (
                        newR in range(rows) and newC in range(cols)
                        and (newR,newC) not in visited and grid[newR][newC] == 1
                    ):
                        res[i] += 1
                        q.append((newR,newC))
                        visited.append((newR,newC))

        
        i = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r,c, i)
                    i+=1

        
        return max(res.values()) if res else 0




        