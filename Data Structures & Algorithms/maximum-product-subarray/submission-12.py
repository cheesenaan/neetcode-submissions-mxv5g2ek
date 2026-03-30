class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # for each i, find maxV and min V
        res = -float('inf')
        maxV = 1
        minV = 1

        for n in nums:
            tempMax = n * maxV
            tempMin = n * minV
            maxV = max(n, tempMax, tempMin)
            minV = min(n, tempMax, tempMin)
            res = max(res, maxV)

        return res


        