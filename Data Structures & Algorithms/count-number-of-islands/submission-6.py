class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols, = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        self.res = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            self.res += 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc

                    if (
                        newR in range(rows) 
                        and newC in range(cols)
                        and (newR, newC) not in visited
                        and grid[newR][newC] == '1'
                    ):
                        q.append((newR, newC))
                        visited.add((newR, newC))


        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == '1':
                    bfs(r,c)

        return self.res


        