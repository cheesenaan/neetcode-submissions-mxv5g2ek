class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s, and t should have same char frequency

        if len(s) != len(t): 
            return False 

        d = {}

        for char in s:
            d[char] = d.get(char, 0) + 1

        print(d)

        for char in t:
            if char not in d.keys():
                return False
            else:
                d[char] = d.get(char, 0) - 1

        print(d)

        for key, val in d.items():
            if val != 0:
                return False

        return True

            

        
        