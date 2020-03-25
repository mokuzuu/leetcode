class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for i in range(n + 1)]
        return self.climb_stairs(0, n, memo)

    def climb_stairs(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb_stairs(
            i + 1, n, memo) + self.climb_stairs(i + 2, n, memo)
        return memo[i]

    def dp_climb_stairs(self, n):
        if n == 1:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def fib_climb_staris(self, n):
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second


print(Solution().climbStairs(19))
print(Solution().dp_climb_stairs(19))
print(Solution().fib_climb_staris(5))
