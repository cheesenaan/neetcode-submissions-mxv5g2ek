class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols, = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            grid[r][c] = '0'
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc

                    if (
                        newR in range(rows) 
                        and newC in range(cols)
                        and grid[newR][newC] == '1'
                    ):
                        q.append((newR, newC))
                        grid[newR][newC] = '0'


        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r,c)
                    res += 1

        return res


        