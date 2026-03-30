class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ######################## solution 1 ########################
        # time and space = O(m*n)
        # dp[i][j] = number of possible paths from [i][j] to [m-1][n-1]
        # dp = [[0] * (n+1) for _ in range(m+1)]
        # dp[m-1][n-1] = 1

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         dp[i][j] += dp[i+1][j] + dp[i][j+1]

        # return dp[0][0]

        ######################## solution 2 ########################
        # O(m*n) time and O(n) space
        # dp = [1] * n # last row is all 1's
        # for _ in range(m-1):
        #     for j in range(n-2, -1, -1):
        #         dp[j] += dp[j+1]

        # return dp[0]

        # Time Complexity: O(1)
        # Space Complexity: O(1)
        # Each path is a permutation of (m-1) downs and (n-1) rights
        # move down (m - 1) times, move right (n - 1) times, overall, you make (m + n - 2) moves
        return math.comb(m + n - 2, m - 1)
