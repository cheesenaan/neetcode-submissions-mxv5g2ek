class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = -float('inf')
        maxV, minV = 1, 1

        for num in nums:

            maxProduct = maxV * num
            minProduct = minV * num
            maxV = max(num, maxProduct, minProduct)
            minV = min(num, maxProduct, minProduct)
            res = max(res, maxV)

        return res

        