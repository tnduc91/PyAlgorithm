# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices) -> int:
    max_profit = 0;
    noOfDays = len(prices)
    if (noOfDays == 0):
        return 0
    
    min_so_far = [prices[0]];
    

    for d in range(1, noOfDays, 1):
        posible_new_max = prices[d] - min_so_far[d-1]
        if max_profit < posible_new_max:
            max_profit = posible_new_max

        if min_so_far[d-1] > prices[d]:
            min_so_far.append(prices[d])
        else:
            min_so_far.append(min_so_far[d-1])

    return max_profit
    

            

output = maxProfit([7,6,4,3,1])
print(output)