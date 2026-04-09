class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        m -= 1
        def distanceCheck(position, balls, d):
            i = 1
            last = position[0] 
            while i < len(position):
                if position[i] - last >= d:
                    last = position[i]
                    balls -= 1
                i += 1

            return balls <= 0


        ans = -1   
        low = 1 
        high = position[-1] - position[0]
        while low <= high:
            mid = (low + high) // 2
            if distanceCheck(position, m, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans