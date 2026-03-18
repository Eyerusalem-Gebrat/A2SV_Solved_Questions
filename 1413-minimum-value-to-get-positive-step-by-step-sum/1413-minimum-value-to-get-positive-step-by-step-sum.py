class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # -3, -1, -4, 0, 2
        # 1, -1, -4

        for i in range(len(nums)):
            if i != 0:
                nums[i] = nums[i-1] + nums[i]

        _min = min(nums)
        if _min >= 1:
            return 1
        else:
            return abs(_min) + 1
