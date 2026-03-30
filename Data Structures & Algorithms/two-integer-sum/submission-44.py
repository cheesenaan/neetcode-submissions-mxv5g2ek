class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hp = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hp and hp[diff] != i:
                return [hp[diff], i]
            hp[num] = i
        return []        