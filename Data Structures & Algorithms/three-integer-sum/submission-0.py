class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2.56

        res = set()
        nums.sort()


        for i in range(0 , len(nums)):
            for j in range(i , len(nums)):
                for k in range(j , len(nums)):
                    if i!=j and i!=k and j!=k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            tmp = [nums[i] , nums[j] , nums[k]]
                            res.add(tuple(tmp))
                            


        return [list(i) for i in res]

