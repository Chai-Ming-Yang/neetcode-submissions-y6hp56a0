class Solution:
    def countSubstrings(self, s: str) -> int:
        T = '#' + '#'.join(s) + '#'
        N = len(T)
        radii = [0] * N
        r = c = 0
        for center in range(N):
            if center < r:
                radii[center] = min(r - center, radii[c*2 - center])
            while (center + radii[center] + 1 < N and
                    center - radii[center] - 1 >= 0 and
                    T[center + radii[center] + 1] == T[center - radii[center] - 1]):
                radii[center] += 1
            if r < center + radii[center]:
                r = center + radii[center]
                c = center
        return (len(s) + sum(radii)) // 2