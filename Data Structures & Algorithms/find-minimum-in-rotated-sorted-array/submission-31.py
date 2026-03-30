class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        minV = nums[0]

        while l <= r:
            m = l + ((r-l)//2)

            if nums[l] <= nums[m] <= nums[r]:
                return min(minV, nums[l])

            minV = min(minV, nums[m])

            if nums[l] <= nums[m]:
                # we are in left sorted section
                # move right
                l = m + 1
            else:
                # move left
                r = m - 1

        return -1
