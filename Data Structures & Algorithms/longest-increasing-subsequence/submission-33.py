from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #o(n^2) time and o(n) space
        # if not nums:
        #     return 0

        # dp = [1] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j]+1)

        # return max(dp)

        if not nums:
            return 0

        tail = []

        for num in nums:
            idx = bisect_left(tail, num)
            if idx == len(tail):
                tail.append(num)
            else:
                tail[idx] = num
        
        return len(tail)

        