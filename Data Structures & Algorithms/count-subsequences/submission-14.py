class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # ============================================
        # 1️⃣ Recursive DFS with Memoization (Top-Down)
        # ============================================
        # Time Complexity: O(m * n) 
        #    - There are at most m*n unique states (i, j) in recursion.
        # Space Complexity: O(m * n) 
        #    - Memo dictionary + recursion stack depth O(m)
        #
        # memo = {}
        # def dfs(i, j):
        #     # Base case: all characters in t matched
        #     if j == len(t):
        #         return 1
        #     # Base case: s is exhausted but t is not
        #     if i == len(s):
        #         return 0
        #     # Return cached result
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     res = 0
        #     if s[i] == t[j]:
        #         # Option 1: match s[i] with t[j]
        #         res += dfs(i + 1, j + 1)
        #         # Option 2: skip s[i] and try later
        #         res += dfs(i + 1, j)
        #     else:
        #         # Skip s[i], t[j] remains
        #         res += dfs(i + 1, j)
        #     memo[(i, j)] = res
        #     return res
        #
        # return dfs(0, 0)


        # ============================================
        # 2️⃣ Bottom-Up DP (2D Array)
        # ============================================
        # Time Complexity: O(m * n) 
        # Space Complexity: O(m * n)
        #
        # m, n = len(s), len(t)
        # dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        #
        # # Base case: empty t can be matched by any suffix of s
        # for i in range(m + 1):
        #     dp[i][n] = 1
        #
        # # Fill dp table bottom-up
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if s[i] == t[j]:
        #             # Option 1: match current characters
        #             dp[i][j] += dp[i + 1][j + 1]
        #             # Option 2: skip s[i]
        #             dp[i][j] += dp[i + 1][j]
        #         else:
        #             # Skip s[i], t[j] remains
        #             dp[i][j] += dp[i + 1][j]
        #
        # return dp[0][0]


        # ============================================
        # 3️⃣ Bottom-Up DP (1D Space-Optimized)
        # ============================================
        # Time Complexity: O(m * n)
        # Space Complexity: O(n)
        #
        # Only store current row since dp[i][j] only depends on dp[i+1][j] and dp[i+1][j+1]
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[n] = 1  # base case: empty t

        # Iterate over s from end to start
        for i in range(m - 1, -1, -1):
            prev = dp[n]  # store dp[i+1][j+1] for diagonal
            for j in range(n - 1, -1, -1):
                temp = dp[j]  # store dp[i+1][j] for next iteration
                if s[i] == t[j]:
                    # Option 1: match s[i] with t[j] (add diagonal)
                    # Option 2: skip s[i] (keep dp[j])
                    dp[j] = dp[j] + prev
                else:
                    # Only skip s[i]
                    dp[j] = dp[j]
                prev = temp  # update prev for next j (diagonal)
        
        return dp[0]
