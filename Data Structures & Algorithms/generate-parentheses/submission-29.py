class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        
        res, cur = [], []

        def backtrack(o, c, n):
            if o == c == n:
                res.append(''.join(cur))

            if o < n:
                cur.append('(')
                backtrack(o+1, c, n)
                cur.pop()
            
            if c < o:
                cur.append(')')
                backtrack(o, c+1, n)
                cur.pop()

        backtrack(0,0,n)
        return res


        