from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # time O(nlogn), space O(n)
        if not nums:
            return 0

        tails = []

        for num in nums:

            # find index to insert num in tails
            idx = bisect_left(tails, num) #O(logn)
            # increasing subsequence
            if idx == len(tails):
                tails.append(num)
            else:
                # replace idx with num
                tails[idx] = num
        return len(tails)

    def index_to_insert(self, arr, target):
        l, r = 0, len(arr)
        while l < r:
            mid = (l + (r - l)) // 2
            if arr[mid] < target:
                # move right
                l = mid + 1
            else:
                r = mid
        return l