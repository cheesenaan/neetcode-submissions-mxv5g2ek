class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        rows, cols = len(heights), len(heights[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(starts):
            visit = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and heights[r][c] <= heights[nr][nc]
                        and (nr, nc) not in visit
                    ):
                        q.append((nr, nc))
                        visit.add((nr, nc))

            return visit

        pacific_starts = [(0,c) for c in range(cols)] + [(r,0) for r in range(rows)]
        altantic_starts = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows)]

        return list(dfs(pacific_starts) & dfs(altantic_starts))

        