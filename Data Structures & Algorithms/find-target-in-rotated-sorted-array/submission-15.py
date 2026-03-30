class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l, r = 0, len(nums)-1

        while l <= r:

            m = l + ((r-l) // 2)
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                # we are in left sorted section
                if nums[l] <= target <= nums[m]:
                    # search left
                    r = m - 1
                else:
                    # search right
                    l = m + 1
            elif nums[m] <= nums[r]:
                # we are in right sorted section
                if nums[m] <= target <= nums[r]:
                    # search right
                    l = m + 1
                else:
                    # search left
                    r = m - 1

        return - 1

        