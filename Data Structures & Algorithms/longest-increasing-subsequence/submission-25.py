from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[i] = the smallest possible ending value
        # of an increasing subsequence of length (i + 1)
        tails = []

        for num in nums:
            # Find the index where 'num' should go in tails
            # This is the first element >= num
            idx = bisect_left(tails, num)

            if idx == len(tails):
                # num is larger than all elements in tails
                # → we can extend the longest increasing subsequence
                tails.append(num)
            else:
                # Replace the element at idx with num
                # This keeps tails sorted and makes the ending value smaller,
                # which gives more room to build longer subsequences later
                tails[idx] = num

        # The length of tails is the length of the LIS
        return len(tails)
