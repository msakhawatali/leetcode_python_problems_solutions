class Solution(object):
    def maxProfit(self, prices):
        
        if not prices:
            return 0
        
        min_price = prices[0] 
        max_profit = 0
        
        for price in prices:
            
            if price < min_price:
                min_price = price
            
            
            curr_profit = price - min_price
            
            
            if curr_profit > max_profit:
                max_profit = curr_profit
                
        return max_profit