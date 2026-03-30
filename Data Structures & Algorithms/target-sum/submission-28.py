class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            new_dict = defaultdict(int)
            for total, count in dp.items():
                new_dict[total + num] += count
                new_dict[total - num] += count
            dp = new_dict
        
        return dp[target]
