class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # at each step can multiply by num, max or min
        # positive, negative switch
        res = -float('inf')
        minV, maxV = 1, 1

        for n in nums:
            tmpMax = n * maxV
            tmpMin = n * minV
            maxV = max(n, tmpMax, tmpMin)
            minV = min(n, tmpMax, tmpMin)
            res = max(res, maxV)

        return res
       