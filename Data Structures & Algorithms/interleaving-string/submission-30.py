class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        hp = defaultdict(bool)
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if (i,j) in hp:
                return hp[(i,j)]
            
            if i < len(s1) and s1[i] == s3[i+j]:
                hp[(i,j)] = dfs(i+1, j)
            
            if j < len(s2) and s2[j] == s3[i+j]:
                hp[(i,j)] = dfs(i, j+1)

            return hp[(i,j)]

        return dfs(0,0)

                
        