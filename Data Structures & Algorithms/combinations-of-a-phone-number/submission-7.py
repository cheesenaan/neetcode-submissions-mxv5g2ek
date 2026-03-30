from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res, cur = [], []

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
        
        def backtrack(i):
            if i == len(digits):
                return res.append(''.join(cur[:]))

            current_digit = digits[i]
            letters = hp[current_digit]
            for letter in letters:
                cur.append(letter)
                backtrack(i+1)
                cur.pop()

        backtrack(0)
        return res
        
        