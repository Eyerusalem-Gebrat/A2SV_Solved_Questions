class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subArrays = 0
        prefixSums = {0 : 1}
        curSum = 0

        for i in range(n):
            curSum += nums[i]
            if curSum - k in prefixSums:
                subArrays += prefixSums[curSum - k]
            if curSum in prefixSums:
                prefixSums[curSum] += 1
            else:
                prefixSums[curSum] = 1

        return subArrays