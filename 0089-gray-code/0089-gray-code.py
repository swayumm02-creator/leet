class Solution:
    def grayCode(self, n: int) -> list[int]:
        res = []
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res