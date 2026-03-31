class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = { 0:cost[0], 1:cost[1] }
        N = len(cost)
        def dp(i):
            if i < 2 or i in memo: return memo[i]
            memo[i] = cost[i] + min(dp(i-1), dp(i-2))
            return memo[i]
        dp(N-1)
        return min(memo[N-1], memo[N-2])