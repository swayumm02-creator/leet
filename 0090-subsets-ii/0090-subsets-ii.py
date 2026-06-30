class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        def backtrack(index: int, path: list[int]):
            res.append(list(path))
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res