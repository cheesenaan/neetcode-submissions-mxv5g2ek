class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        
        d1 = {}
        for x in s:
            if x not in d1:
                d1[x] = 1
            else:
                d1[x] = d1[x] + 1

        d2 = {}
        for x in t:
            if x not in d2:
                d2[x] = 1
            else:
                d2[x] = d2[x] + 1

        return d1 == d2
            

        
        