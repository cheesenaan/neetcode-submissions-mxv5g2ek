class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        set_s = set(s)
        set_t = set(t)

        if set_s != set_t:
            return False

        
        dict_s = {}
        for x in s:
            if x in dict_s:
                print("adding one")
                dict_s[x] = dict_s[x] + 1
            else:
                print("setting one")
                dict_s[x] = 1

        dict_t = {}
        for x in t:
            if x in dict_t:
                dict_t[x] = dict_t[x] + 1
            else:
                dict_t[x] = 1

        return dict_s == dict_t


        




        
        