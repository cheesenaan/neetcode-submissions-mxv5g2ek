class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        
        res, cur = [], []

        def dfs(total, i):
            if total == target:
                return res.append(cur[:])

            if total > target or i == len(candidates):
                return 

            # current candidates[i] unlimited number of times
            cur.append(candidates[i])
            dfs(total + candidates[i], i+1)
            cur.pop()
            # skip candidates[i] 

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1

            dfs(total, i+1)

        dfs(0,0)
        return res



        

        