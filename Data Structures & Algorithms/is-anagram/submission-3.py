class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s, and t should have same char frequency

        if len(s) != len(t):
            return False

        dict_s = {}
        for char in s:
            if char in dict_s.keys():
                dict_s[char] += 1
            else:
                dict_s[char] = 1
            
        
        dict_t = {}
        for char in t:
            if char in dict_t.keys():
                dict_t[char] += 1
            else:
                dict_t[char] = 1

        print(dict_s)
        print(dict_t)

        return dict_s == dict_t

            

        
        