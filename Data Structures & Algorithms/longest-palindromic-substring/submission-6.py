class Solution:
    def longestPalindrome(self, s: str) -> str:

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(self.res):
                    self.res = s[l:r+1]
                l = l - 1
                r = r + 1
        
        self.res = ''

        for i in range(len(s)):
            # odd
            helper(i,i)

            # even
            helper(i,i+1)

            
        return self.res

        