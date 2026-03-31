class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums)
        N = len(nums)
        dp1 = nums[:]; dp1[1] = max(dp1[0], dp1[1])
        dp = nums[:]; dp[0] = 0
        for i in range(2, N):
            dp[i] = max(dp[i] + dp[i-2], dp[i-1])
            dp1[i] = max(dp1[i] + dp1[i-2], dp1[i-1])
        
        return max(dp1[-2], dp[-1])