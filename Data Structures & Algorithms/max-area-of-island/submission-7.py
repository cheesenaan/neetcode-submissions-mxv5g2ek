class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        dimensions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        self.maxArea = 0

        # def bfs(r, c):
        #     q = deque()

        #     q.append((r,c))
        #     visited.add((r,c))

        #     area = 1

        #     while q:
        #         r, c = q.popleft()

        #         for dr, dc in dimensions:
        #             newRow = dr + r
        #             newCol = dc + c

        #             if (
        #                 newRow in range(rows) and newCol in range(cols)
        #                 and grid[newRow][newCol] == 1
        #                 and (newRow, newCol) not in visited
        #             ):
        #                 q.append((newRow, newCol))
        #                 visited.add((newRow,newCol))
        #                 area += 1
            
        #     return area

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0  # mark visited
            area = 1  # count current cell

            # Explore all 4 directions
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.maxArea = max(dfs(r,c), self.maxArea)

        return self.maxArea



        

        