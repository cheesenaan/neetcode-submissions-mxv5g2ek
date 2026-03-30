class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        from bisect import bisect_left
        tail = []

        for n in nums:
            idx = bisect_left(tail,n)
            if idx == len(tail):
                tail.append(n)
            else:
                tail[idx] = n

        return len(tail)