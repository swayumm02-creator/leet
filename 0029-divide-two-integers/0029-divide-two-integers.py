class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
            
        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        while a >= b:
            temp, mul = b, 1
            while a >= (temp << 1):
                temp <<= 1
                mul <<= 1
            a -= temp
            res += mul
            
        return sign * res   