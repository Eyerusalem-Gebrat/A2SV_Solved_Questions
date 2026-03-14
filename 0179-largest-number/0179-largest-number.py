class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string = list(map(str, nums))

        def whoFirst(num1, num2):
            if num1 + num2 > num2 + num1:
                return -1
            elif num1 + num2 < num2 + num1:
                return 1
            else:
                return 0

        string.sort(key=cmp_to_key(whoFirst))
        
        if string[0] == "0":
            return "0"
        
        return "".join(string)