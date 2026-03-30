class Solution:

    def ListNode(self, val, n):
        self.val = val
        self.next = n

    def findDuplicate(self, nums: List[int]) -> int:

        # define linked list data structure
        # for each num in nums, add to linked list
        # after each additon check if already exists

        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num

        return -1


