class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(height) - 1
        while l < r :
            if height[l] < height[r]:
                water = height[l] * (r - l)
                l += 1
            else:
                water = height[r] * (r - l)
                r -= 1

            maxWater = max(maxWater, water)

        return maxWater