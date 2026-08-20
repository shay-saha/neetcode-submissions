class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 100000000000
        maxprofit = 0
        for price in prices:
            minprice = min(minprice,price)
            profit = price - minprice
            if profit> maxprofit:
                maxprofit = profit
        return maxprofit

        
