class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        N = len(nums)
        memo = { 0:nums[0], 1:max(nums[0], nums[1]) }
        def dp(i):
            if i in memo: return memo[i]
            memo[i] = max(nums[i] + dp(i-2), dp(i-1))
            return memo[i]
        dp(N-1)
        print(memo.values())
        return max(memo[N-1], memo[N-2])