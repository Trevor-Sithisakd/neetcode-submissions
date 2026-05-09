class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers one at each end prioritise moving the one that if its legal move the one that is considered lower cant use greedy here
        i = 0
        j = 1
        profit = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = max(profit, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return profit