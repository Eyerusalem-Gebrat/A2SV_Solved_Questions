class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur_sum = sum(nums[:k])
        j = 0
        for i in range(k, len(nums)):
            cur_sum += (nums[i] - nums[j])
            j += 1
            max_sum = max(cur_sum, max_sum)

        return (max_sum / k)
