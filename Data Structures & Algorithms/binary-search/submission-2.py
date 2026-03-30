class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            # mid = int((r + l ) / 2) # r + l can overflow if sum > max integer threshold 2^31
            mid = l + int((r-l)/2) # to prevent overflow

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

       