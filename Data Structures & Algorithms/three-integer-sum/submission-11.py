class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort 
        # for each element in nums, seperate then call two sum

        nums.sort()
        res = []

        for i in range(len(nums)):
            # skip duplicates from first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lp = i + 1
            rp = len(nums) -1
            while lp < rp:
                s = nums[i] + nums[lp] + nums[rp]
                if s == 0:
                    res.append([nums[i] , nums[lp] , nums[rp]])
                    
                    # skip duplicates for remaining
                    while lp < rp and nums[lp] == nums[lp+1]:
                        lp = lp + 1
                    
                    while lp < rp and nums[rp] == nums[rp-1]:
                        rp = rp -1

                    lp = lp + 1
                    rp = rp - 1

                elif s > 0:
                    rp = rp - 1
                elif s < 0:
                    lp = lp + 1

        return res
                
            