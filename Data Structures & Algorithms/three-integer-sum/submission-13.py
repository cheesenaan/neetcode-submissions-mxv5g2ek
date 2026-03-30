class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # brute force O(n^3) time and O(n) space

        # optimized
        # sort nums
        # for each i in nums, call two sum with two pointers
        # checks to skip duplicates

        nums.sort()

        res = []

        for i in range(len(nums)):
            # skip duplicates on i
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            l,r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                print(s)
                if s == 0:
                    res.append([nums[i] , nums[l] , nums[r]])

                    #skip duplicates on l 
                    while l < r and nums[l] == nums[l+1]:
                        l = l + 1

                     #skip duplicates on r
                    while l < r and nums[r] == nums[r-1]:
                        r = r - 1

                    l = l + 1
                    r = r - 1
                elif s > 0:
                    r = r - 1
                elif s < 0:
                    l = l + 1

        return res
                



        