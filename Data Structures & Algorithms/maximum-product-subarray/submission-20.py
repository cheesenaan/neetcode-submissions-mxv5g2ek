class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = -float('inf')
        maxV, minV = 1, 1

        for n in nums:
            tempMax = n * maxV
            tempMin = n * minV
            maxV = max(n, tempMax, tempMin)
            minV = min(n, tempMax, tempMin)
            res = max(res, maxV)

        return res
        