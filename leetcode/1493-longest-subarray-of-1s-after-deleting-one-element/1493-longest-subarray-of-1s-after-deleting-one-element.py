class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        zeros = 0

        left = 0 
        right = 0
        while right < len(nums):
            if nums[right] == 1:
                right += 1
            elif nums[right] == 0:
                zeros += 1
                right += 1
            
            while zeros > 1 and left < len(nums):
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            longest = max(longest, right - left - 1)

        return longest