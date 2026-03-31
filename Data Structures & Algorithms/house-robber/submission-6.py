class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        p2, p = nums[0], max(nums[:2])
        N = len(nums)
        for i in range(2, N):
            p2, p = p, max(nums[i] + p2, p)
        return max(p2, p)