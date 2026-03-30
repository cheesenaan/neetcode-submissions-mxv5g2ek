class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) -1
        minN = nums[r]
        
        while l <= r:
            if l > r:
                return minN

            m = l + ((r-l)//2) # prevent overflow

            minN = min(minN, nums[m])

            if nums[m] > nums[r]:
                # search right
                l = m + 1
            else:
                # search left
                r = m - 1

        return minN


       