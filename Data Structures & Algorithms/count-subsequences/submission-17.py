class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)

        hp = {}
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0

            if (i,j) in hp:
                return hp[(i,j)]

            res = 0
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
                res += dfs(i+1, j)
            else:
                res += dfs(i+1, j)
            
            hp[(i,j)] = res
            return res

        return dfs(0,0)

            