class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        is_pal = [[False] * n for _ in range(n)]
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            min_cuts = n - i - 1
            
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
                    
                    if j == n - 1:
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, 1 + dp[j + 1])
                        
            dp[i] = min_cuts
            
        return dp[0]