class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        res = float('inf')
        N = len(coins)
        def dp(i, remain, used):
            nonlocal res, N
            if remain == 0:
                res = min(res, used); return
            if i == N:
                return
            for j in range(remain // coins[i], -1, -1):
                if j + used > res: break
                dp(i+1, remain - coins[i] * j, used + j)
        dp(0, amount, 0)
        return -1 if res==float('inf') else res