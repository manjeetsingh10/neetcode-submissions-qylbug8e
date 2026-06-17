class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        # compute minimum at every iteration. or while going ahead
        minimum = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            sellValue = prices[i]
            profit = max(sellValue - minimum, profit)
            minimum = min(minimum, prices[i])
        
        return profit