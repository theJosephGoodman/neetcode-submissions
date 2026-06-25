class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_point = 0
        highest_point = 0

        for i in range(len(prices)):
            if prices[i] - prices[lowest_point] > max_profit:
                max_profit = prices[i] - prices[lowest_point]
                highest_point = i
            if prices[i] < prices[lowest_point]:
                lowest_point = i
        return max_profit