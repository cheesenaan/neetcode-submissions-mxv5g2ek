class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n+1)

        for i in range(1, n+1):
            # The number of 1s in i equals the number of 1s in i without the last bit, plus 1 if the last bit is ON
            dp[i] = dp[i >> 1] + (i & 1)

        return dp


        