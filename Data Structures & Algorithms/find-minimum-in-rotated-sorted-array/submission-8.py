class Solution:
    def findMin(self, nums: List[int]) -> int:

        minV = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:

            if nums[l] < nums[r]:
                minV = min(minV, nums[l])
                break

            m = l + ((r-l) // 2)
            minV = min(nums[m], minV)

            if nums[m] >= nums[l]:
                # we are in left sorted section
                # search right for min
                l = m + 1
            else:
                # we are in right sorted section
                # search left
                r = m - 1

        return minV

        