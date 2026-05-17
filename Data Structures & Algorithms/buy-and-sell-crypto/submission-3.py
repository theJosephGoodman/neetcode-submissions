class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        point1, point2 = 0,1
        max_profit = 0

        while point2 < len(prices):
            current_profit = prices[point2] - prices[point1]

            max_profit = max(max_profit, current_profit)


            if prices[point1] > prices[point2]:
                point1 = point2
        
            point2+=1
        return max_profit