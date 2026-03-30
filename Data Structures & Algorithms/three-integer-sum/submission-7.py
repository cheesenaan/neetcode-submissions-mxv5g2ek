class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lp , rp = i+1, len(nums) -1
            while lp < rp:
                s = nums[i] + nums[lp] + nums[rp]
                if s == 0:
                    if [nums[i] , nums[lp] , nums[rp]] not in res:
                        res.append([nums[i] , nums[lp] , nums[rp]])

                        # Skip duplicates for left and right pointers
                        while lp < rp and nums[lp] == nums[lp+1]:
                            lp = lp + 1

                        while lp < rp and nums[rp] == nums[rp - 1]:
                            rp = rp - 1

                        lp = lp + 1
                        rp = rp - 1

                elif s < 0:
                    lp = lp + 1
                elif s > 0:
                    rp = rp -1
            

        return res
                


        