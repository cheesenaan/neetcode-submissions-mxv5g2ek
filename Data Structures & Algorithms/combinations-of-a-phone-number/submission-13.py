from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


        res = []
        cur = []

        if not digits:
            return res

        hp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            if i >= len(digits):
                return res.append(''.join(cur[:]))

            letters = hp[digits[i]]
            for letter in letters:
                cur.append(letter)
                dfs(i+1)
                cur.pop()

        dfs(0)
        return res

        