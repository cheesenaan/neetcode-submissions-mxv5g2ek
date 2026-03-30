class Solution:
    def rob(self, nums: List[int]) -> int:


        return max(self.isHelper(nums[1:]),self.isHelper(nums[:-1]) , nums[0])


    def isHelper(self, arr):
        rob1, rob2 = 0, 0
        for n in arr:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

      