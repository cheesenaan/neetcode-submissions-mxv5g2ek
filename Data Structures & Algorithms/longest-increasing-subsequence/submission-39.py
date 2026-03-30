from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        tails = []

        for n in nums:
            idx = bisect_left(tails, n)
            if idx == len(tails):
                tails.append(n)
            else:
                tails[idx] = n
        #print("tails is ", tails)
        return len(tails)

        