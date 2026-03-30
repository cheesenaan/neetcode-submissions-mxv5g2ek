class Solution:
    def numDecodings(self, s: str) -> int:
        
        # ------------------------------------------------------------
        # APPROACH 1: Brute force recursion with memoization (Top-down DP)
        # ------------------------------------------------------------
        # Time: O(n) with memoization
        # Space: O(n) for recursion stack + memo dictionary
        #
        # This approach defines dfs(i) as the number of ways to decode
        # the substring starting at index i (s[i:]).

        # memo = {}
        
        # def dfs(i):
        #     # BASE CASE:
        #     # If we have consumed the entire string (or gone past it),
        #     # that means we found one valid decoding.
        #     if i >= len(s):
        #         return 1

        #     # INVALID CASE:
        #     # A substring starting with '0' cannot be decoded.
        #     if s[i] == '0':
        #         return 0
            
        #     # MEMOIZATION:
        #     # If we've already computed dfs(i), reuse the result.
        #     if i in memo:
        #         return memo[i]

        #     # OPTION 1:
        #     # Decode one digit and move forward by one index.
        #     count = dfs(i + 1)

        #     # OPTION 2:
        #     # Decode two digits if:
        #     # 1) There are at least two characters left
        #     # 2) The two-digit number is between 10 and 26
        #     if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
        #         count += dfs(i + 2)

        #     # Store result in memo and return it
        #     memo[i] = count
        #     return count

        # return dfs(0)

        # ------------------------------------------------------------
        # APPROACH 2: Bottom-up DP using an array
        # ------------------------------------------------------------
        # Time: O(n)
        # Space: O(n)
        #
        # dp[i] = number of ways to decode the first i characters (s[0:i])

        # if not s or s[0] == '0':
        #     return 0

        # dp = [0] * (len(s) + 1)

        # BASE CASES:
        # dp[0] = 1 -> one way to decode an empty string
        # dp[1] = 1 -> first character is guaranteed non-zero here
        # dp[0], dp[1] = 1, 1

        # for i in range(2, len(s) + 1):
        #     # CASE 1: One-digit decode
        #     # If the last character is not '0',
        #     # we can extend all decodings up to i-1
        #     if s[i - 1] != '0':
        #         dp[i] += dp[i - 1]

        #     # CASE 2: Two-digit decode
        #     # If the last two characters form a number between 10 and 26,
        #     # we can extend all decodings up to i-2
        #     if s[i - 2] != '0':
        #         if 10 <= int(s[i - 2:i]) <= 26:
        #             dp[i] += dp[i - 2]

        # return dp[-1]

        # ------------------------------------------------------------
        # APPROACH 3: Optimized Bottom-up DP (O(1) space)
        # ------------------------------------------------------------
        # Time: O(n)
        # Space: O(1)
        #
        # This is the optimal solution.
        # Instead of storing the entire dp array, we only keep:
        # prev1 = dp[i-1]
        # prev2 = dp[i-2]

        # Edge case:
        # An empty string or a string starting with '0' cannot be decoded.
        if not s or s[0] == '0':
            return 0

        # Initialization:
        # prev2 corresponds to dp[0] (empty string)
        # prev1 corresponds to dp[1] (first character)
        prev2, prev1 = 1, 1

        # Iterate through the string starting from the second character
        for i in range(2, len(s) + 1):
            curr = 0  # dp[i]

            # CASE 1: One-digit decode
            # If the current character is not '0',
            # it can be decoded on its own.
            if s[i - 1] != '0':
                curr += prev1

            # CASE 2: Two-digit decode
            # Check if the last two characters form a valid number (10–26)
            if s[i - 2] != '0':
                if 10 <= int(s[i - 2:i]) <= 26:
                    curr += prev2

            # Slide the window forward:
            # dp[i-2] <- dp[i-1]
            # dp[i-1] <- dp[i]
            prev2 = prev1
            prev1 = curr

        # prev1 now holds the number of ways to decode the entire string
        return prev1
