class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        profit = 0
        for sellday in range(len(prices)):
            for buyday in range(0,sellday):
                profit = prices[sellday] - prices[buyday]
                if profit > maxprofit:
                    maxprofit = profit
        return maxprofit
