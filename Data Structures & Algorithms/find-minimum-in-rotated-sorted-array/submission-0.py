class Solution:
    def findMin(self, nums: List[int]) -> int:


        # sort array in place O(1)
        nums.sort()


        # binary search
        l , r = 0 , len(nums) - 1
        minV = nums[0]

        while l <= r:
            if l > r:
                return -1

            m = l + ((r-l)//2)
            if nums[m] <= minV:
                minV = nums[m]
                r = m - 1
            else:
                l = m + 1

        return minV


