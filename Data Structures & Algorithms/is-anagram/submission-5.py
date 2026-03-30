class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s, and t should have same char frequency

        if len(s) != len(t): 
            return False 
        d = {}

        for char in s:
            d[char] = d.get(char, 0) + 1

        for char in t:
            if char not in d:
                return False
            else:
                d[char] -= 1

        return all(val == 0 for val in d.values())


            

        
        