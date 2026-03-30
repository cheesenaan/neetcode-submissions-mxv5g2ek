class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        ####################### SOLUTION 1 #######################
        # If total lengths don't match, s3 cannot be formed
        # if len(s1) + len(s2) != len(s3):
        #     return False
        
        dp = {}  # memoization: (i, j) -> True/False

        def dfs(i, j):
            # i = number of characters taken from s1
            # j = number of characters taken from s2
            # current index in s3 is i + j

            # If we've used all characters from both s1 and s2,
            # we have successfully formed s3
            if i == len(s1) and j == len(s2):
                return True

            # If this state has already been computed, return cached result
            if (i, j) in dp:
                return dp[(i, j)]

            res = False

            # Option 1: take next character from s1 if it matches s3
            if i < len(s1) and s1[i] == s3[i + j]:
                res = dfs(i + 1, j)

            # Option 2: take next character from s2 if it matches s3
            # We still try this even if option 1 failed
            if j < len(s2) and s2[j] == s3[i + j]:
                res = dfs(i, j + 1)

            # Store result for this state to avoid recomputation
            dp[(i, j)] = res
            return dp[(i, j)]

        # Start with 0 characters taken from both strings
        
        #return dfs(0, 0)

        ####################### SOLUTION 2 #######################
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]


