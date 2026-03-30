class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cur = []
        res = 0        
        def dfs(i):
            nonlocal res
            if i == len(s):
                temp = ''.join(cur[:])
                if temp == t:
                    res += 1
                    return
                return 0

            cur.append(s[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)

        dfs(0)
        return res
        