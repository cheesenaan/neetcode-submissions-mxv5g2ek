from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        

        hp = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r', 's'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y', 'z']
        }

        res, cur = [], []
        def dfs(i):
            if i == len(digits):
                return res.append(''.join(cur[:]))

            current_digit = digits[i]
            letters = hp[current_digit]
            for letter in letters:
                cur.append(letter)
                dfs(i+1)
                cur.pop()

        dfs(0)
        return res