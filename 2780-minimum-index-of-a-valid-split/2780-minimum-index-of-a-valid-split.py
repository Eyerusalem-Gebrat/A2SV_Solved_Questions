from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxFreq = max(freq.values())
        dominant = None
        for key, val in freq.items():
            if val == maxFreq:
                dominant = key
        
        for i in range(len(nums) - 1):
            f1 = 0
            f2 = 0
            for num in nums[:i+1]:
                if num == dominant:
                    f1 += 1
            f2 = maxFreq - f1
            if f1 * 2 > len(nums[:i+1]) and f2 * 2 > len(nums[i+1:]):
                return i
            
        return -1