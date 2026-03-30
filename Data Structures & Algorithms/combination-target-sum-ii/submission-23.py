class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res, cur = [], []
        candidates.sort()

        def backtrack(total, i):
            if total == target:
                return res.append(cur[:])
            
            if total > target or i >= len(candidates):
                return 
            
            # current may be chosen at most once within a combination
            cur.append(candidates[i])
            backtrack(total + candidates[i], i+1)

            cur.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(total, i+1)

        backtrack(0,0)
        return res