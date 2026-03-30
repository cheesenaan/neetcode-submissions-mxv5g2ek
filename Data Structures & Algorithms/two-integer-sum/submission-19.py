class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {} # num as key and index as value

        for i , n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [ hashMap[diff], i ]
            hashMap[n] = i


            



        
