class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # at each i, max can either be itself, product of n and max or n and min
        res, maxV, minV = -float('inf'),1,1

        for n in nums:
            tempMax = n * maxV
            tempMin = n * minV
            maxV = max(n, tempMax, tempMin)
            minV = min(n, tempMax, tempMin)
            res = max(res, maxV, minV)

        return res

        
        