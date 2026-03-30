class Solution:
    def numDecodings(self, s: str) -> int:
        

        # memo = {}
        # def dfs(i):
        #     if i >= len(s):
        #         return 1
            
        #     if s[i] == '0':
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     res = dfs(i+1)

        #     if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
        #         res += dfs(i+2)

        #     memo[i] = res
        #     return res

        # return dfs(0)

        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        
        res = 0 
        for i in range(2, n+1):

            # choice 1 : single digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # choice 2 : two digits
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]


        return dp[n]

        