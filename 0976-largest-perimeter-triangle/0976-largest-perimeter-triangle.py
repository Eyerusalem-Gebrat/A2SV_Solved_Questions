class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) == 3:
            _max = max(nums)
            _sum = sum(nums)
            if _sum - _max > _max:
                return _sum
            else: return 0
   
        nums.sort(reverse=True)
        left = 0
        for i in range(len(nums) - 2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]

        return 0