class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #O(1)

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        
        return False

            


