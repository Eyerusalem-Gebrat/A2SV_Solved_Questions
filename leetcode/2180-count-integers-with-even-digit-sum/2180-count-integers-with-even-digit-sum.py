class Solution:
    def countEven(self, num: int) -> int:
        count = 0

        for i in range(1, num + 1):
            digit_sum = 0
            x = i
            while x > 0:
                digit_sum += x % 10
                x //= 10
            if digit_sum % 2 == 0:
                count += 1

        return count