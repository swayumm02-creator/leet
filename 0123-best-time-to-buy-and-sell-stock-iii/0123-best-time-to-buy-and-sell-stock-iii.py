class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
            
        buy1 = float('-inf')
        buy2 = float('-inf')
        profit1 = 0
        profit2 = 0
        
        for price in prices:
            buy1 = max(buy1, -price)
            profit1 = max(profit1, buy1 + price)
            buy2 = max(buy2, profit1 - price)
            profit2 = max(profit2, buy2 + price)
                
        return profit2