class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            m = l + ((r-l)//2)

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if nums[l] <= target <= nums[m]:
                    # move left
                    r = m - 1
                else:
                    # move right
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1


        
        return -1

            

        