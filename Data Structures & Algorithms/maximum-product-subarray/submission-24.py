class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res keeps track of the maximum product subarray seen so far
        res = -float('inf')

        # maxV = maximum product ending at the current index
        # minV = minimum product ending at the current index
        # We track minV because multiplying by a negative number
        # can turn a small (negative) product into a large positive one
        maxV, minV = 1, 1

        # Iterate through each number in the array
        for n in nums:
            # Temporarily store products before updating maxV and minV
            tempMax = maxV * n
            tempMin = minV * n

            # The new max product ending here can be:
            # 1) the current number alone (start a new subarray)
            # 2) extend the previous max product subarray
            # 3) extend the previous min product subarray (if n is negative)
            maxV = max(n, tempMax, tempMin)

            # Similarly, compute the new minimum product ending here
            minV = min(n, tempMax, tempMin)

            # Update the global maximum product
            res = max(res, maxV)

        # Return the maximum product of any contiguous subarray
        return res
