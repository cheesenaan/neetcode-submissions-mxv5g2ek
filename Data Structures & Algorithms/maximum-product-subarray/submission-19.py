class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        # At each index, the maximum product subarray ending there can come from:
        # the current number itself, the previous max product times the current number,
        # or the previous min product times the current number — because a negative can flip signs.
        # So I track both max and min products and update them in O(1) space
        
        # maxV = maximum product of a subarray that ENDS at the current index
        # minV = minimum product of a subarray that ENDS at the current index

        
        res = -float('inf')
        maxV, minV = 1, 1

        for n in nums:
            tempMax = maxV * n
            tempMin = minV * n
            maxV = max(n, tempMax, tempMin)
            minV = min(n, tempMax, tempMin)
            res = max(res, maxV)

        return res
