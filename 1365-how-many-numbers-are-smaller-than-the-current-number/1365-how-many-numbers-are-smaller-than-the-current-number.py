class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        _max = max(nums)
        count = [0] * (_max + 1)

        for i in range(n):
            count[nums[i]] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1] 

        ans = []
        for num in nums:
            if num == 0:
                ans.append(0)
            else:
                ans.append(count[num-1])

        return ans