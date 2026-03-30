class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        dimensions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        self.maxArea = 0

        def bfs(r, c):
            q = deque()

            q.append((r,c))
            visited.add((r,c))

            area = 1

            while q:
                r, c = q.popleft()

                for dr, dc in dimensions:
                    newRow = dr + r
                    newCol = dc + c

                    if (
                        newRow in range(rows) and newCol in range(cols)
                        and grid[newRow][newCol] == 1
                        and (newRow, newCol) not in visited
                    ):
                        q.append((newRow, newCol))
                        visited.add((newRow,newCol))
                        area += 1
            
            return area

        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    self.maxArea = max(bfs(r,c), self.maxArea)

        return self.maxArea



        

        