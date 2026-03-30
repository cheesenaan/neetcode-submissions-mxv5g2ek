class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        nums.sort()
        print(nums)
        l, r = 0, 1
        while l < len(nums) and r < len(nums):
            if nums[l] != nums[r]:
                return nums[l]
            l += 2
            r += 2

        return nums[-1]
        