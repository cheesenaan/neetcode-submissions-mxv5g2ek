class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == '0':
            return 0

        # dp[i] = number of decodings at i for s[:i]
        n = len(s)
        # dp = [0] * (n+1)
        # dp[0], dp[1] = 1, 1
        prev2, prev1 = 1, 1

        for i in range(2, n+1):
            curr = 0
            # choice 1: choose 1 digit
            if s[i-1] != '0':
                curr += prev1

            # choice 2: choose 2 digits
            if 10 <= int(s[i-2:i]) <= 26:
                curr += prev2

            prev2 = prev1
            prev1 = curr
        
        return prev1





        