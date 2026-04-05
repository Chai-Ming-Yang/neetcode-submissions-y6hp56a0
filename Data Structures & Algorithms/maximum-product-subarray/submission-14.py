class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        res = mx = mn = nums[0]
        for i in range(1, N):
            if nums[i] > 0:
                mx = max(nums[i], nums[i] * mx)
                if mn < 0:  mn = min(nums[i], nums[i] * mn)
                else:   mn = max(nums[i], mn * nums[i])
            else:
                tmpMx = mx
                mx = max(nums[i], mn * nums[i])
                mn = min(nums[i], tmpMx * nums[i])
            res = max(res, mx)
        return res