class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        
        def dfs(str1: str, str2: str) -> bool:
            if (str1, str2) in memo:
                return memo[(str1, str2)]
                
            if str1 == str2:
                memo[(str1, str2)] = True
                return True
                
            if sorted(str1) != sorted(str2):
                memo[(str1, str2)] = False
                return False
                
            n = len(str1)
            for i in range(1, n):
                # Case 1: No swap at the current root
                if dfs(str1[:i], str2[:i]) and dfs(str1[i:], str2[i:]):
                    memo[(str1, str2)] = True
                    return True
                
                # Case 2: Swap occurred at the current root
                if dfs(str1[:i], str2[n-i:]) and dfs(str1[i:], str2[:n-i]):
                    memo[(str1, str2)] = True
                    return True
                    
            memo[(str1, str2)] = False
            return False
            
        return dfs(s1, s2)