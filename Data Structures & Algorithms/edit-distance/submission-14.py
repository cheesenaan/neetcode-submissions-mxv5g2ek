class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        hp = defaultdict(int)
        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i

            if i == len(word1):
                return len(word2) - j

            if (i,j) in hp:
                return hp[(i,j)]

            if word1[i] == word2[j]:
                hp[(i,j)] = dfs(i+1, j+1)
            else:
                hp[(i,j)] = min(
                    1 + dfs(i+1, j+1),
                    1 +  dfs(i+1, j),
                    1 +  dfs(i, j+1)
                )

            return hp[(i,j)]

        return dfs(0,0)



        