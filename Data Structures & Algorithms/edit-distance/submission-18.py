class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        hp = {}
        def dfs(i, j):
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

            if (i,j) in hp:
                return hp[(i,j)]

            if word1[i] == word2[j]:
                hp[(i,j)] = dfs(i+1, j+1)
            else:
                insert = 1 + dfs(i+1, j+1)
                delete  = 1 + dfs(i, j+1)
                replace  = 1 + dfs(i+1, j)
                hp[(i,j)] = min(insert, delete, replace)

            return hp[(i,j)]

        return dfs(0,0)


            
        