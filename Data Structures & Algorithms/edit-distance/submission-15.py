class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        from collections import defaultdict

        # hp = memoization dictionary to store results of dfs(i,j)
        # Key: (i, j) → indices in word1 and word2
        # Value: minimum operations to convert word1[i:] → word2[j:]
        hp = defaultdict(int)

        def dfs(i, j):
            """
            Returns the minimum number of operations to convert
            word1[i:] into word2[j:]
            """

            # Base Case 1:
            # If we have exhausted word2, we only need to delete
            # all remaining characters in word1
            if j == len(word2):
                return len(word1) - i

            # Base Case 2:
            # If we have exhausted word1, we only need to insert
            # all remaining characters of word2
            if i == len(word1):
                return len(word2) - j

            # If result is already computed, return from memo
            if (i, j) in hp:
                return hp[(i, j)]

            # If current characters match, no operation needed
            if word1[i] == word2[j]:
                hp[(i, j)] = dfs(i + 1, j + 1)
            else:
                # Characters don't match, consider all three operations:
                # 1) Replace current character: 1 + dfs(i+1, j+1)
                # 2) Delete from word1: 1 + dfs(i+1, j)
                # 3) Insert into word1: 1 + dfs(i, j+1)
                hp[(i, j)] = min(
                    1 + dfs(i + 1, j + 1),  # replace
                    1 + dfs(i + 1, j),      # delete
                    1 + dfs(i, j + 1)       # insert
                )

            # Return the computed minimum distance
            return hp[(i, j)]

        # Start from the beginning of both strings
        return dfs(0, 0)
