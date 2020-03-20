def rob(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    dp = []
    dp[0] = 0
    dp[1] = nums[0]
    for idx in range(1, len(nums)):
        dp[idx + 1] = max([dp[idx], dp[idx - 1] + nums[idx]])

    return dp[-1]
