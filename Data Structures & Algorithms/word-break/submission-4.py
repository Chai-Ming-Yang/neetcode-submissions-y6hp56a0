class Solution:
    def wordBreak(self, s: str, wordDict: Set[str]) -> bool:
        L = len(s)
        dp = [False] * (L + 1)
        dp[0] = True
        mxL = max({len(st) for st in wordDict})

        for i in range(L):
            if not dp[i]: continue
            for j in range(1, min(mxL+1, L+1-i)):
                if s[i:i+j] in wordDict:
                    dp[i+j] = True
        return dp[L]