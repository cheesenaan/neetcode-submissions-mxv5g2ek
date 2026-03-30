class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # num as key and index as value
        hashMap = {} 

        for i , n in enumerate(nums):  #O(n) time and space
            diff = target - n
            if diff in hashMap:
                return [ hashMap[diff], i ]
            hashMap[n] = i


            



        
