class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            if i >= len(s):
                return 1
            
            if s[i] == '0':
                return 0

            # first letter
            count = dfs(i+1)

            # second letter
            if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                count += dfs(i+2)

            return count

        return dfs(0)