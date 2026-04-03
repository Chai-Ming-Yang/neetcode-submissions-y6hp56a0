class Solution:
    def countSubstrings(self, s: str) -> int:
        S = '#' + '#'.join(s) + '#'
        radii = [0] * len(S)
        c = r = 0

        for center in range(0, len(S)):
            # if center inside rightmost palindrome
            if center < r:
                mirror = c * 2 - center
                radii[center] = min(r - center, radii[mirror])
            
            while (center + radii[center] + 1 < len(S) and
                    center - radii[center] - 1 >= 0 and
                    S[center + radii[center] + 1] == S[center - radii[center] - 1]):
                radii[center] += 1
            
            if center + radii[center] > r:
                r = center + radii[center]
                c = center
        
        return (len(s) + sum(radii))//2