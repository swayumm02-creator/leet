class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        
        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + jump)
            
        return True  