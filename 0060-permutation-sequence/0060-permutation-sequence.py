class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        nums = []
        for i in range(1, n):
            fact *= i
            nums.append(i)
        nums.append(n)
        
        k -= 1
        res = []
        
        while True:
            res.append(str(nums[k // fact]))
            nums.pop(k // fact)
            if not nums:
                break
            k %= fact
            fact //= len(nums)
            
        return "".join(res)