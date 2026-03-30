class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hp = {num:i for i, num in enumerate(nums)}
        print("hp is", hp)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hp and hp[diff] != i:
                return [i, hp[diff]]
        return []        