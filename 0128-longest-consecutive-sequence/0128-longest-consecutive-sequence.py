class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        _nums = set(nums)
        for num in _nums:
            if num - 1 not in _nums:
                length = 1
                current = num
                while current + 1 in _nums:
                    length += 1
                    current += 1
                count = max(count, length)

        return count