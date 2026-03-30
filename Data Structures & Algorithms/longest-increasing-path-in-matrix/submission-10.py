class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        indegree = [[0 for j in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and matrix[nr][nc] < matrix[r][c]
                    ):
                        indegree[r][c] += 1

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if  indegree[r][c] == 0:
                    q.append((r,c))

        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and matrix[nr][nc] > matrix[r][c]
                    ):
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append((nr, nc))

            level += 1

        return level
            



        