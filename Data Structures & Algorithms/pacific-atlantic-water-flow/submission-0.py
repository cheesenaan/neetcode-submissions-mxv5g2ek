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
        pacific_starts = []
        atlantic_starts = []

        for r in range(rows):
            pacific_starts.append((r, 0))
            atlantic_starts.append((r , cols-1))

        for c in range(cols):
            pacific_starts.append((0, c))
            atlantic_starts.append((rows-1 , c))

        pacific_reachable, atlantic_reachble = bfs(pacific_starts), bfs(atlantic_starts)

        # common elements from pacific and atlantic

        return list(pacific_reachable & atlantic_reachble)

