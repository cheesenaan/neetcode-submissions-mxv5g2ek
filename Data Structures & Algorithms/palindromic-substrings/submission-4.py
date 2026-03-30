class Solution:
    def countSubstrings(self, s: str) -> int:

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.res += 1
                l = l - 1
                r = r + 1
        
        self.res = 0

        for i in range(len(s)):
            # odd
            helper(i,i)

            # even
            helper(i,i+1)

            
        return self.res

        

        