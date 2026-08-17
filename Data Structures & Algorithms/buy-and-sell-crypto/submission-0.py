class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy cheap sell high
        # input one day and sell the most expensive day

        # should I look over this prices?
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price< min_price:
                min_price = price
            else:
                profit = price-min_price
                max_profit = max(max_profit,profit)

        return max_profit