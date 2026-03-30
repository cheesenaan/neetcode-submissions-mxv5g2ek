class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 9.19 pm
        # 9.26 pm
        
        distinct_nums = set(nums) #O(n) time and space

        d = {}
        for num in distinct_nums: #O(n) time and space
            d[num] = 0

        for num in nums: #O(n)
            d[num] += 1 #O(1)
            if d[num] >= 2:
                return True

        return False
        

         