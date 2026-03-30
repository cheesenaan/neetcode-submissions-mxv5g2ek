class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # O(1) space for initializing an empty set
        for num in nums:  # O(n) to iterate over the list
            if num in seen:  # O(1) average case for checking membership in the set
                return True  # O(1) to return a boolean
            seen.add(num)  # O(1) average case for adding an element to the set
        return False  # O(1) to return a boolean
