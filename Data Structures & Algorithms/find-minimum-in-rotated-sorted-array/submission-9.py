class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1
        res = nums[r]

        while l <= r:

            # if already sorted and not rotated
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            m = l + ((r-l) // 2)
            res = min(nums[m], res)

            if nums[l] <= nums[m]:
                # we are in left sorted section
                # search right
                l = m + 1
            else:
                r = m - 1

        return res
