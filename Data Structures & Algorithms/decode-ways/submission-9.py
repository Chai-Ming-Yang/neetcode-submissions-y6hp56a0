class Solution:
    def numDecodings(self, s: str) -> int:
        """ top down recursion """
        memo = { len(s) : 1}
        def dp(i):
            if i in memo: return memo[i]
            if s[i] == '0': return 0
            memo[i] = dp(i+1)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                memo[i] += dp(i+2)
            return memo[i]
        return dp(0)