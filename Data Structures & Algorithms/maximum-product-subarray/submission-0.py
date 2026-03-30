class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # dp[i] = min and max up to nums[:i]

        res = max(nums)
        minValue, maxValue = 1, 1

        for n in nums:

            tempMax = maxValue * n
            tempMin = minValue * n
            maxValue = max(n,tempMax, tempMin)
            minValue = min(n,tempMax, tempMin)
            res = max(res,maxValue )

        return res

