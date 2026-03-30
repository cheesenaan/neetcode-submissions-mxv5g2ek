class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #O(1) time and space complexity

        for num in nums: #O(n) time and O(1) space complexity
            if num not in seen: #O(1) time and space complexity
                seen.add(num) #O(1) time and space complexity
            else:
                return True #O(1) time and space complexity

        return False #O(1) time and space complexity
