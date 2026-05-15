class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_revenue = 0

        while r<len(prices):
            
            # profitable?
            if prices[l] < prices[r]:
                total_revenue = prices[r] - prices[l]
                max_revenue = max(max_revenue, total_revenue)

            # non-profitable?
            if prices[l] > prices[r]:
                l = r
            r+=1
        return max_revenue
                