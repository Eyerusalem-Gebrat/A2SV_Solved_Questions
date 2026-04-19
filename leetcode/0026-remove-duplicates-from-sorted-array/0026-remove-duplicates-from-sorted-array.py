class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        for right in range(1, len(nums)):
            if nums[unique] != nums[right]:
                unique += 1
                nums[unique] = nums[right]
        return unique + 1
