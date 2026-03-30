class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols, = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0

        def dfs(r, c):
            # q = deque()
            # q.append((r,c))
            area = 1
            stack = []
            stack.append((r,c))
            grid[r][c] = 0
            while stack:
                # r, c = q.popleft()
                r, c = stack.pop()
                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc

                    if (
                        newR in range(rows) 
                        and newC in range(cols)
                        and grid[newR][newC] == 1
                    ):
                        stack.append((newR, newC))
                        grid[newR][newC] = 0
                        area += 1

            return area

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))

        return res


        

        


        