class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        minV = nums[r]

        while l <= r:
            if nums[l] <= nums[r]:
                minV = min(minV, nums[l])
                break

            m = l + ((r-l) // 2)
            minV = min(minV, nums[m])

            if nums[l] <= nums[m]:
                # search right
                l = m + 1
            else:
                # search left
                r = m - 1

        return minV

        