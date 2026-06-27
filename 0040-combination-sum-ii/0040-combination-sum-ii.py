class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        
        def backtrack(remain, combo, start):
            if remain == 0:
                res.append(list(combo))
                return
            if remain < 0:
                return
                
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                combo.append(candidates[i])
                backtrack(remain - candidates[i], combo, i + 1)
                combo.pop()
                
        backtrack(target, [], 0)
        return res