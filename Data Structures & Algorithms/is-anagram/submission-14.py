class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): #O(1) time and O(1) space
            return False

        
        d1 = {}  #O(n) time and O(1) space because we only have 26 chars
        for x in s:
            if x not in d1:
                d1[x] = 1
            else:
                d1[x] = d1[x] + 1

        d2 = {} #O(n) time and O(1) space because we only have 26 chars
        for x in t:
            if x not in d2:
                d2[x] = 1
            else:
                d2[x] = d2[x] + 1

        return d1 == d2
            

        
        