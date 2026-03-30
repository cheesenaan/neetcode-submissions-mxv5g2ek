class Solution:
    def climbStairs(self, n: int) -> int:

        # brute force o(2^n) time and o(n) space

        # res, cur = [], []
        # def dfs(i):
        #     if i == n:
        #         return res.append(cur[:])
            
        #     if i > n:
        #         return

        #     cur.append(i+1)
        #     dfs(i+1)
        #     cur.pop()

        #     cur.append(i+2)
        #     dfs(i+2)
        #     cur.pop()

        # dfs(0)
        # return len(res)

        # o(n) time and space cashing with array
        if n <= 2:
            return n

        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]



        