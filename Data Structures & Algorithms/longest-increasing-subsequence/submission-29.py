from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        tails = []

        for num in nums:

            # find index to insert num in tails
            idx = bisect_left(tails, num)
            # increasing subsequence
            if idx == len(tails):
                tails.append(num)
            else:
                # replace idx with num
                tails[idx] = num
        return len(tails)


        
        