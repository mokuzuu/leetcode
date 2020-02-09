class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = n
        for i in range(1, n+1):
            if coins >= i:
                coins = coins - i
            else:
                return i - 1


print(Solution().arrangeCoins(8))
