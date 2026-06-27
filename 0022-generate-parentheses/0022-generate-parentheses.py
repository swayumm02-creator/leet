class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_n: int, closed_n: int, path: list[str]):
            if open_n == closed_n == n:
                res.append("".join(path))
                return
                
            if open_n < n:
                path.append("(")
                backtrack(open_n + 1, closed_n, path)
                path.pop()
                
            if closed_n < open_n:
                path.append(")")
                backtrack(open_n, closed_n + 1, path)
                path.pop()
                
        backtrack(0, 0, [])
        return res