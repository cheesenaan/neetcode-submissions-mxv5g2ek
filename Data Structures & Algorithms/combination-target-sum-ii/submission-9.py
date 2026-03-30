class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res, curr = [],[]

        def dfs(t, i):
            if t == target:
                return res.append(curr[:])

            if t > target or i == len(candidates):
                return None

            # current
            curr.append(candidates[i])
            dfs(t + candidates[i], i+1)
            curr.pop()

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(t,i+1)

        dfs(0,0)
        return res
        