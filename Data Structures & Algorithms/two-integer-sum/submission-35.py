class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {} #value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hp:
                return[hp[diff], i]
            hp[n] = i


        return []

        

       
        

        