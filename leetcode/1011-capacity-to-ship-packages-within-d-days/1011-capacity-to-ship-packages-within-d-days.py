class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(cap):
            _sum = 0
            d = 1
            for i in range(len(weights)):
                if _sum + weights[i] > cap:
                    d += 1
                    _sum = weights[i]
                else:
                    _sum += weights[i]
  
            return d <= days

        low = max(weights)
        high = sum(weights)
        while low <= high:
            cap = (low + high) // 2
            if possible(cap):
                high = cap - 1
            else:
                low = cap + 1

        return low
