class Solution:
    def __init__(self):
        return
        


    def maxProfit_brute_force(self, prices):
        def inner_max_profit(prices):
            length = len(prices)
            if (length == 0):
                return 0
            max_profit = 0
            for i in range(length):
                for j in range(i + 1, length):
                    profit = prices[j] - prices[i]
                    profit += inner_max_profit(prices[j+1:length])
                    max_profit = max(max_profit, profit)
            return max_profit

        return inner_max_profit(prices)

    def max_profit_peak_valley(self, prices):
        max = 0
        length = len(prices)

        if (length < 2):
            return 0
        
        peak = prices[0]
        valley = prices[0]

        for i in range(length):
            if prices[i] > peak:
                peak = prices[i]
            else:
                max += (peak - valley)
                peak = prices[i]
                valley = prices[i]
        
        return max

