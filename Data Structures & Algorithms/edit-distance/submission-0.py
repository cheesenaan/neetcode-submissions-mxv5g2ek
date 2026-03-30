class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # memo[(i, j)] will store the minimum edit distance
        # to convert word1[i:] -> word2[j:]
        memo = {}

        def dfs(i, j):
            # BASE CASE 1:
            # If we've used all characters of word1,
            # we must insert all remaining characters of word2
            if i == len(word1):
                return len(word2) - j

            # BASE CASE 2:
            # If we've used all characters of word2,
            # we must delete all remaining characters of word1
            if j == len(word2):
                return len(word1) - i

            # If this subproblem was already solved, reuse it
            if (i, j) in memo:
                return memo[(i, j)]

            # If current characters match,
            # no operation is needed — move both pointers
            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
            else:
                # INSERT:
                # Insert word2[j] into word1 at position i
                # So j moves forward, i stays the same
                insert = 1 + dfs(i, j + 1)

                # DELETE:
                # Delete word1[i]
                # So i moves forward, j stays the same
                delete = 1 + dfs(i + 1, j)

                # REPLACE:
                # Replace word1[i] with word2[j]
                # So both pointers move forward
                replace = 1 + dfs(i + 1, j + 1)

                # Choose the operation with minimum cost
                res = min(insert, delete, replace)

            # Store result in memo to avoid recomputation
            memo[(i, j)] = res
            return res

        # Start converting full word1 to full word2
        return dfs(0, 0)
