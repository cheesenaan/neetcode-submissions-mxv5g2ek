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
            # Base case: we have processed all digits
            if i == len(digits):
                res.append(''.join(cur))
                return

            # Get letters for the current digit
            current_digit = digits[i]
            for letter in hp[current_digit]:
                cur.append(letter)
                dfs(i + 1)  # Move to next digit
                cur.pop()   # Backtrack

        dfs(0)
        return res
