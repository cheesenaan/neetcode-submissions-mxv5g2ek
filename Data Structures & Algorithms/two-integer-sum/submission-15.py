class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have a hashmap to store value -> index
        # for each num in nums, find the diff.
        # if diff in hashmap we have answer


        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i ]
            else:
                hashmap[num] = i
        
