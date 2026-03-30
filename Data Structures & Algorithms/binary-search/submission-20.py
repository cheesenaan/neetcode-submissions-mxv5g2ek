class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:

            m = l + ((r-l) // 2)

            if nums[m] == target:
                return m
            elif nums[m] > target:
                # search on lower half
                r = m - 1
            elif nums[m] < target:
                # search on upper half
                l = m + 1

        return -1