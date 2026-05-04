class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = False
        profit = 0
        buyprice = 0
        dp = {}

        def dfs(i, holding) : 
            if i >= len(prices) : 
                return 0
            if (i, holding) in dp : 
                return dp[(i, holding)]
            
            if not holding : 
                buy = dfs(i+1, not holding) - prices[i] 
                cooldown = dfs(i+1, holding)
                dp[(i, holding)] = max(buy, cooldown)
            else : 
                sell = dfs(i+2, not holding) + prices[i]
                cooldown = dfs(i+1, holding) 
                dp[(i, holding)] = max(sell, cooldown)
            return dp[(i, holding)]
        return dfs(0, 0)