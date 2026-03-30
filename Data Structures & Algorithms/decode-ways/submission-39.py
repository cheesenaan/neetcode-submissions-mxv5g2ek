class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        
        # dp[i] = number of decodings at index i for s[:i]
        prev2, prev1 = 1, 1

        for i in range(2, len(s)+1):
            cur = 0
            # take only 1 digit
            if s[i-1] != '0':
                cur += prev1

            # take 2 digits
            if 10 <= int(s[i-2:i]) <= 26:
                cur += prev2
            
            prev2 = prev1
            prev1 = cur

        return prev1

        