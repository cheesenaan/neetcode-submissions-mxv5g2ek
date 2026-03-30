class Solution:
    def findMin(self, nums: List[int]) -> int:


        # binary search O(logn)
        l , r = 0 , len(nums) - 1
        minV = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minV = min(minV, nums[l])
                break

            m = (l + r) // 2
            minV = min(minV, nums[m])
            if nums[m] >= nums[l]:
                # search to the right
                l = m + 1
            else:
                # search to the left
                r = m - 1

        return minV