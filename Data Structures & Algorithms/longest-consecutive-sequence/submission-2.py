class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exist = set(nums)
        res = 0
        for i in exist:
            length = 1
            while i + 1 in exist:
                length += 1
                i += 1
            res = max(length, res)
        return res