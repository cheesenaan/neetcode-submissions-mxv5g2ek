class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        
        # dp[i] = number of decodings at index i for s[:i]
        dp = [0] * (len(s)+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, len(s)+1):
            # take only 1 digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # take 2 digits
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[-1]

        