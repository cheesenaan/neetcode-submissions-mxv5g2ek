class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        minV = float('inf')

        while l <= r:
            m = l + ((r-l)//2)

            # already sorted
            if nums[l] <= nums[m] <= nums[r]:
                minV = min(minV, nums[l])
                break

            minV = min(minV, nums[m])

            #find pivot
            if nums[l] <= nums[m]:
                # we are in left sorted section
                # move right
                l = m + 1
            else:
                r = m - 1

        return minV


