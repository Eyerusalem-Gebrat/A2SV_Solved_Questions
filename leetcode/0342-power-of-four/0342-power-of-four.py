class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def powerOfFour(num):
            if num == 1: 
                return True
            if num < 1:
                return False

            return powerOfFour(num / 4)
        
        return powerOfFour(n)
