class Solution:
    def hammingWeight(self, n: int) -> int:
        # res = 0
        # while n > 0:
        #     print("n is : ", n)
        #     res += n % 2
        #     n = n >> 1
        # return res

        res = 0
        while n > 0:
            n = n & (n-1)
            res += 1
        return res
        