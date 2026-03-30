class Solution:
    def numDecodings(self, s: str) -> int:
        
        # brute force o(n) time and o(n) space
        # memo = {}
        
        # def dfs(i):
        #     if i >= len(s):
        #         return 1

        #     if s[i] == '0':
        #         return 0
            
        #     if i in memo:
        #         return memo[i]

        #     # first letter
        #     count = dfs(i+1)

        #     # second letter
        #     if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
        #         count += dfs(i+2)

        #     return count

        # return dfs(0)

        # o(n) time and o(n) space
        # if not s or s[0] == '0':
        #     return 0

        # dp = [0] * (len(s)+1)

        # dp[0], dp[1] = 1, 1

        # for i in range(2, len(s)+1):
        #     # check last digit
        #     if s[i-1] != '0':
        #         dp[i] += dp[i-1]

        #     # check last two digits
        #     if s[i-2] != '0':
        #         if 10 <= int(s[i-2:i]) <= 26:
        #             dp[i] += dp[i-2]

        # return dp[-1]

        
        # o(n) time and o(1) space
        if not s or s[0] == '0':
            return 0


        prev2, prev1 = 1, 1

        for i in range(2, len(s)+1):
            curr = 0
            # check last digit
            if s[i-1] != '0':
                curr += prev1

            # check last two digits
            if s[i-2] != '0':
                if 10 <= int(s[i-2:i]) <= 26:
                    curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1
