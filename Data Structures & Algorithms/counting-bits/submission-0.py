class Solution:
    def countBits(self, n: int) -> List[int]:

        def count1s(n):
            res = 0
            while n > 0:
                n = n & (n-1)
                res += 1
            return res
        
        output = [0] * (n+1)

        for i in range(n+1):
            output[i] = count1s(i)

        return output

        