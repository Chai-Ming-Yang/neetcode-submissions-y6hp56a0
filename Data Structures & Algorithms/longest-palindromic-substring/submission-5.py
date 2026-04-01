class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        N = len(s)

        def pal(l, r):
            while 0 <= l and r < N:
                if s[l] != s[r]: return
                nonlocal res
                if r+1-l > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        for i in range(N):
            pal(i, i)   # odd
            pal(i, i+1) # even
        return res