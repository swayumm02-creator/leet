class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def backtrack(start: int, comb: list[int]):
            if len(comb) == k:
                res.append(list(comb))
                return
                
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
                
        backtrack(1, [])
        return res