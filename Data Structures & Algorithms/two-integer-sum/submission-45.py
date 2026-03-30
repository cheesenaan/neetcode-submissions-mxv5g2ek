class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hp = {} # num -> index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hp:
                return [hp[diff], i]
            hp[num] = i
        return []