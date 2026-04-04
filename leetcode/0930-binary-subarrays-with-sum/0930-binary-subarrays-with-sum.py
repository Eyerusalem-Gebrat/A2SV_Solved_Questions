class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # prefix sum count
        count = {0: 1}  
        curr_sum = 0
        result = 0

        for num in nums:
            curr_sum += num

            if (curr_sum - goal) in count:
                result += count[curr_sum - goal]

            if curr_sum in count:
                count[curr_sum] += 1
            else:
                count[curr_sum] = 1

        return result