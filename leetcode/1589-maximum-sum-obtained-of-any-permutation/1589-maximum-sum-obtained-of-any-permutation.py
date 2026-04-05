class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        
        freq = [0] * (n + 1)
        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1
        
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
        freq = freq[:-1]  
        
        nums.sort()
        freq.sort()
        MOD = 10**9 + 7
        result = 0
        
        for a, b in zip(nums, freq):
            result = (result + a * b) % MOD
        
        return result