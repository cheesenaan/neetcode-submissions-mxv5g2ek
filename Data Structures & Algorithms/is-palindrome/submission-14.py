class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1

        while l < r:
            while l<r and self.isAlphanumeric(s[l]) == False:
                l = l + 1

            while l<r and self.isAlphanumeric(s[r]) == False:
                r = r - 1

            if s[l].lower() != s[r].lower():
                return False
            
            l = l + 1
            r = r - 1
        
        return True

            
    def isAlphanumeric(self, char):
        if '0' <= char <= '9' or  'a' <= char <= 'z' or  'A' <= char <= 'Z':
            return True
        return False


        
