class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        arr = []
        nums.sort()

        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if i!=j and i!=k and k!=j:
                        if nums[i] + nums[j] + nums[k] == 0:
                            tmp = [nums[i], nums[j], nums[k]]
                            if tmp not in arr:
                                arr.append(tmp)

        return arr

