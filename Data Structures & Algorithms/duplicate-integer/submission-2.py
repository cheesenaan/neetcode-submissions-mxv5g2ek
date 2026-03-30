class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 9.19 pm
        # 9.26 pm

        d = {}
        for num in nums: #O(n) time and space
            d[num] = 0

        for num in nums: #O(n)
            d[num] += 1 #O(1)
            if d[num] >= 2:
                return True

        return False
        

         