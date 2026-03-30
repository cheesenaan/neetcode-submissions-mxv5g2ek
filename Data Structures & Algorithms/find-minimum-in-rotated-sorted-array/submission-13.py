class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        minV = nums[0]

        while l <= r:
            m = l + ((r-l) // 2)

            if nums[l] <= nums[r]:
                minV = min(minV, nums[l])
                break

            minV = min(minV, nums[m])

            if nums[l] <= nums[m]:
                # we are in left sorted section
                # search right
                l = m + 1
            else:
                # we are in right sorted section
                r = m - 1

        return minV





        