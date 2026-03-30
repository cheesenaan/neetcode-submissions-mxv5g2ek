from collections import deque

class Solution:
    # Time Complexity: O(m * n)
    #   - Each cell is processed once when its in-degree becomes 0.
    #   - For each cell, we check up to 4 neighbors.
    #
    # Space Complexity: O(m * n)
    #   - indegree matrix stores the in-degree for each cell.
    #   - Queue can hold up to O(m*n) cells in worst case.

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # Possible directions: down, up, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Compute in-degree for each cell
        # indegree[r][c] = number of neighbors smaller than cell (r,c)
        indegree = [[0 for j in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check bounds and if neighbor is smaller
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[r][c]:
                        indegree[r][c] += 1

        # Initialize queue with all cells that have in-degree 0 (sources)
        # These are the starting points of increasing paths
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if indegree[r][c] == 0:
                    q.append((r, c))

        # BFS / topological sort
        # Each layer corresponds to one step in the longest increasing path
        level = 0
        while q:
            # Process all nodes in the current layer
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Only consider neighbors that are greater (valid increasing move)
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                        indegree[nr][nc] -= 1  # Remove dependency
                        # If neighbor now has no incoming edges, add to queue
                        if indegree[nr][nc] == 0:
                            q.append((nr, nc))
            # One BFS layer completed → corresponds to one step in the path
            level += 1

        # The number of BFS layers = length of longest increasing path
        return level
