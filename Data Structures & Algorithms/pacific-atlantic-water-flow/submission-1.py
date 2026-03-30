class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(starts):
            q = deque(starts)
            visited = set(starts)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and heights[r][c] <= heights[nr][nc]
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited
        
        # bfs from pacific 
        # bfs from atlantic

        pacific_starts = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlantic_starts = [(r , cols-1) for r in range(rows)] + [(rows-1 , c) for c in range(cols)]

        # common elements from pacific and atlantic

        return list(bfs(pacific_starts) & bfs(atlantic_starts))

