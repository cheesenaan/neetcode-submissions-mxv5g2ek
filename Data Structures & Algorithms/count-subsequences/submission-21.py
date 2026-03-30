class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        hp = defaultdict(int)
        def dfs(i, j):
            if j == len(t):
                return 1

            if not (i < len(s) and j < len(t)):
                return 0

            if (i,j) in hp:
                return hp[(i,j)]

            if s[i] == t[j]:
                hp[(i,j)] += dfs(i+1,j+1)
                hp[(i,j)] += dfs(i+1,j)
            else:
                hp[(i,j)] += dfs(i+1,j)

            return hp[(i,j)]

        return dfs(0,0)
                
        