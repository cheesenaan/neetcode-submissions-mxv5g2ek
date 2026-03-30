class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hp = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hp:
                return [hp[diff], i]
            hp[nums[i]] = i
        return []

        