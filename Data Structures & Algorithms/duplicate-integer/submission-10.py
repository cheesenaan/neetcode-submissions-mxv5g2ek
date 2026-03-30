class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set() #O(1) time and O(1) space

        for num in nums: #O(n) time and O(1) space
            if num in seen: #O(1) time and O(1) space
                return True #O(1) time and O(1) space
            else:
                seen.add(num) #O(1) time and O(n) space

        return False #O(1) time and O(1) space


        #O(n) time and O(n) space
       
        
        
            


