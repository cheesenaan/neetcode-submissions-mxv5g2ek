class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]


        def bfs(starts):
            visited = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and heights[r][c] <= heights[nr][nc]
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited
        
        # Pacific starts
        pacific_starts = [(0,c) for c in range(cols)] + [(r,0) for r in range(rows)]

        # Atantic starts
        atlantic_starts = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows)]

        # dfs starting from Pacific and Atantic
        # return intersection of Pacific and Atantic dfs
        return list(bfs(pacific_starts) & bfs(atlantic_starts))



        


        