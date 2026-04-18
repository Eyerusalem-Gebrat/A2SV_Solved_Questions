class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        num = 0
        string = ""
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append((string, num))
                num = 0
                string = ""
            elif char == "]":
                prev_str, cur_num = stack.pop()
                string = prev_str + string * cur_num
            else:
                string += char

        return string