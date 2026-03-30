class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # if s[i] == t[j] -> i+1,j+1 and i+1,j
        # else i+1,j

        def dfs(i,j):
            if j == len(t):
                return 1

            if not (i < len(s) and j < len(t)):
                return 0

            res = 0
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
                res += dfs(i+1, j)
            else:
                res += dfs(i+1, j)

            return res


        return dfs(0,0)
        