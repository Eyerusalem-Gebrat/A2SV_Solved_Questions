class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        multiple = {0: -1}
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]

        for i in range(len(nums)):
            cur = nums[i] % k
            if cur in multiple:
                if i - multiple[cur] >= 2:
                    return True
            else:
                multiple[cur] = i

        return False 