class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, arr):
        rob1, rob2 = 0, 0
        for n in arr:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
