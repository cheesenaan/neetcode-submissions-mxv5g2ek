class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == '0':
            return 0
        
        # dp[i] = number of encodings for substring s[:i]
        # n = len(s)
        # dp = [0] * (n+1)
        # dp[0] = 1 # empty 
        # dp[1] = 1 # garanteed since != 0

        # for i in range(2, n+1):
        #     # choice 1 : take one digit
        #     if s[i-1] != '0':
        #         dp[i] += dp[i-1]

        #     # choice 2 : take two digits
        #     if 10 <= int(s[i-2:i]) <= 26:
        #         dp[i] += dp[i-2]

        # return dp[n]

        n = len(s)
        prev2, prev1 = 1, 1
        for i in range(2, n+1):
            curr = 0
            # choice 1 : take one digit
            if s[i-1] != '0':
                curr += prev1

            # choice 2 : take two digits
            if 10 <= int(s[i-2:i]) <= 26:
                curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1



        