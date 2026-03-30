class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort() 
        res, curr = [], []

        def dfs(total, i):
            if total == target:
                return res.append(curr[:])

            if total > target or i >= len(candidates):
                return

            # current
            curr.append(candidates[i])
            dfs(total + candidates[i], i+1)
            curr.pop()

            #skip
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1

            dfs(total, i+1)


        dfs(0,0)
        return res
            

        