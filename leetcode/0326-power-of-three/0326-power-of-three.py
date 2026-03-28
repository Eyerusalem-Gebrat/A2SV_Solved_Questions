class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def powerOfThree(num):
            if num == 1:
                return True
            if num < 1 or num % 3 != 0:
                return False
            return powerOfThree(num // 3)
        
        return powerOfThree(n)