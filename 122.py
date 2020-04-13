# BRUTE FORCE
# class Solution:
#     def maxProfit(self, prices) -> int:
#         return self.calculate(prices, 0)

#     def calculate(self, prices, s):
#         if s >= len(prices):
#             return 0
#         m = 0
#         for start in range(s, len(prices)):
#             max_profit = 0
#             for i in range(start + 1, len(prices)):
#                 if prices[start] < prices[i]:
#                     profit = self.calculate(
#                         prices, i + 1) + prices[i] - prices[start]
#                     if profit > max_profit:
#                         max_profit = profit

#             if max_profit > m:
#                 m = max_profit
#         return m

# Simple one pass


class Solution:
    def maxProfit(self, prices) -> int:
        if prices is None or len(prices) == 0:
            return 0
        profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit


print(Solution().maxProfit([7, 1, 5, 3, 4]))
# print(Solution().maxProfit([1, 2, 3, 4, 5]))
# print(Solution().maxProfit([7, 6, 5, 4, 3,  1]))
