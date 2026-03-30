class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(i,j,s):

            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
            
        
        res, cur = [], []

        def dfs(i):
            if i == len(s):
                return res.append(cur[:])

            for j in range(i, len(s)):
                if isPalindrome(i,j,s):
                    cur.append(s[i:j+1])
                    dfs(j+1)
                    cur.pop()
        
        dfs(0)
        return res
