class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # dp[i] = max product at nums[i] for nums[:i]
        res = -float('inf')
        # at each i, track max and min value
        maxV, minV = 1, 1

        for n in nums:
            tempMax = maxV * n
            tempMin = minV * n
            maxV = max(n, tempMax, tempMin)
            minV = min(n, tempMax, tempMin)
            res = max(res, maxV)

        return res