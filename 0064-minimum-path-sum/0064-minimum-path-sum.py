class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n
        dp[0] = 0
        
        for r in range(m):
            for c in range(n):
                if c == 0:
                    dp[c] += grid[r][c]
                else:
                    dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
                    
        return dp[-1]