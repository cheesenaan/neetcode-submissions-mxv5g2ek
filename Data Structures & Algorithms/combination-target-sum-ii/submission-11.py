class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res, cur = [], []

        def dfs(t, i):
            if t == target:
                return res.append(cur[:])

            if t > target or i == len(candidates):
                return None

            # include
            cur.append(candidates[i])
            dfs(t + candidates[i], i + 1)
            cur.pop()

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1

            dfs(t, i + 1)

        dfs(0,0)
        return res

        