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
            # best case
            if i == len(digits):
                print("curr found", ''.join(cur))
                return res.append(''.join(cur))

            current_digit = digits[i]
            for d in hp[current_digit]:
                cur.append(d)
                dfs(i+1)
                cur.pop()

        
        dfs(0)
        return res

        