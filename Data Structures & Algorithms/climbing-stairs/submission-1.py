class Solution:
    def climbStairs(self, n: int) -> int:
        p, c = 0, 1
        for _ in range(n):
            p, c = c, p+c
        return c